from app.core.database import get_db
from app.models.mfa import UserMFAMethod
from app.models.user import User
import pyotp

def setup_totp(db, user):
    mfa_record = db.query(UserMFAMethod).filter(
        UserMFAMethod.user_id == user.id,
        UserMFAMethod.method_type == "totp",
        UserMFAMethod.is_verified == False
    ).first()

    secret = pyotp.random_base32()

    if not mfa_record:
        mfa_record = UserMFAMethod(
            user_id=user.id,
            method_type="totp",
            secret_configuration=secret,
            is_primary=True 
        )
        db.add(mfa_record)
    else:
        mfa_record.secret_configuration = secret

    db.commit()
    return secret

def verify_totp(db, user, token):
    mfa_record = db.query(UserMFAMethod).filter(
        UserMFAMethod.user_id == user.id,
        UserMFAMethod.method_type == "totp",
        UserMFAMethod.is_verified == False
    ).first()

    if not mfa_record:
        return False

    totp = pyotp.TOTP(mfa_record.secret_configuration)
    is_valid = totp.verify(token)

    if is_valid:
        mfa_record.is_verified = True
        db.commit()

    return is_valid

def disable_mfa(db, user):
    mfa_record = db.query(UserMFAMethod).filter(
        UserMFAMethod.user_id == user.id,
        UserMFAMethod.method_type == "totp"
    ).first()

    if mfa_record:
        db.delete(mfa_record)
        db.commit()
        return True
    return False