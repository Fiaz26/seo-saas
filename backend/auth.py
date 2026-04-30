from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.models import User
from jose import jwt

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_token(username: str):
    return jwt.encode(
        {"sub": username},
        SECRET_KEY,
        algorithm=ALGORITHM
    )


from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class SignupRequest(BaseModel):
    username: str
    password: str

@router.post("/auth/signup")
def signup(data: SignupRequest):
    return {"api_key": create_api_key(data.username)}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.username)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


from backend.apikey import create_api_key

@router.post("/generate-key")
def generate_key(username: str):
    return {"api_key": create_api_key(username)}


from backend.admin import upgrade_user_plan0



@router.post("/upgrade")
def upgrade(username: str, plan: str):
    return upgrade_user_plan(username, plan)
