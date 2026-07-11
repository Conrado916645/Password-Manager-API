import pyotp
from fastapi import APIRouter, Depends, HTTPException, Request, logger
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.database import get_db
from app.core.security import verify_password
from app.models.user import User
from app.models.mfa import UserMFAMethod
from app.schemas.mfa_totp import DisableMFASchema, VerifyMFASchema
from app.api.dependencies import get_base_user, get_current_user, require_permission
from app.core.rate_limit import limiter
from app.services.mfa_totp import setup_totp, verify_totp

router = APIRouter()

@router.get("/mfa/setup/totp")
async def setup_totp(
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):  
    secret = setup_totp(db, current_user)
    logger.info(f"User '{current_user.username}' initiated TOTP setup. Secret generated.")
    return {"secret": secret}


@router.post("/mfa/verify/totp")
async def verify_totp(
    payload: VerifyMFASchema, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    verification_result = verify_totp(db, current_user, payload.token)
    if not verification_result:
        logger.warning(f"User '{current_user.username}' failed TOTP verification with token: {payload.token}")
        raise HTTPException(status_code=400, detail="Invalid verification code.")
    logger.info(f"User '{current_user.username}' successfully verified TOTP setup.")
    return {"message": "Authenticator App successfully linked!"}

@router.post("/mfa/disable")
@limiter.limit("5/minute")
async def disable_mfa(
    request: Request,
    payload: DisableMFASchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    disable_mfa(db, current_user)
    logger.info(f"MFA successfully disabled for user {current_user.username}")
    return {"message": "Two-Factor Authentication has been completely disabled."}