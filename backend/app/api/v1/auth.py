from fastapi import APIRouter, HTTPException

from backend.db.database import SessionLocal
from backend.models.auth_models import LoginRequest, RegisterRequest
from backend.models.user import User
from backend.services.auth_service import AuthService

auth_router = APIRouter()

auth_service = AuthService()


@auth_router.post("/register")
def register(request: RegisterRequest):

    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == request.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(
        email=request.email, password_hash=auth_service.hash_password(request.password)
    )

    db.add(user)

    db.commit()

    return {"message": "User created"}


@auth_router.post("/login")
def login(request: LoginRequest):

    db = SessionLocal()

    user = db.query(User).filter(User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not (auth_service.verify_password(request.password, user.password_hash)):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth_service.create_token(str(user.id))

    return {"access_token": token}
