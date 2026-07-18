#(Backend API)

The core REST API and backend service for the  architecture. Built as a secure, local-first application, this backend provides robust infrastructure monitoring, zero-knowledge credential management, and secure VPN gateway administration.

---

## 🚀 Core Features

* **Local-First Architecture:** Designed to run securely on local infrastructure without forced external cloud dependencies.
* **VPN Manager:** Centralized CRUD management for remote gateways, pre-shared keys (PSK), and connection credentials.
* **Zero-Knowledge Password Vault:** Secure credential storage utilizing client-side AES-GCM encryption and RSA-OAEP key wrapping. The backend strictly handles ciphertext and never accesses plaintext passwords.
* **Advanced Authentication:** Secure user sessions protected by JWT (JSON Web Tokens) and Time-based One-Time Password (TOTP) Multi-Factor Authentication.
* **System Administration:** Built-in role-based access control (RBAC), user lifecycle management, and system health endpoints.

## 🛠️ Technology Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - High-performance, asynchronous web framework.
* **Database & ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) with SQLite (configurable for PostgreSQL).
* **Data Validation:** [Pydantic](https://docs.pydantic.dev/) - Strict type checking and payload validation.
* **Security & Cryptography:** `passlib` (bcrypt hashing), `python-jose` (JWT handling), and `pyotp` (MFA generation).

---

## ⚙️ Local Development Setup

Follow these steps to configure and run the backend environment locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/infra-sentinel-backend.git](https://github.com/yourusername/infra-sentinel-backend.git)
cd infra-sentinel-backend
