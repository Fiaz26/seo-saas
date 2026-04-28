from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from backend.app.db.database import get_connection
from backend.app.core.security import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(email: str, password: str):
    conn = get_connection()
    cur = conn.cursor()

    hashed = bcrypt.hash(password)

    try:
        cur.execute(
            "INSERT INTO users (email, password, plan) VALUES (?, ?, 'free')",
            (email, hashed)
        )
        conn.commit()
    except:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"message": "User created", "plan": "free"}

@router.post("/login")
def login(email: str, password: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cur.fetchone()

    if not user or not bcrypt.verify(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(email)

    return {
        "access_token": token,
        "token_type": "bearer",
        "plan": user["plan"]
    }

# 🔥 PRO UPGRADE ENDPOINT (mock upgrade for now)
@router.post("/upgrade-to-pro")
def upgrade(email: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("UPDATE users SET plan='pro' WHERE email=?", (email,))
    conn.commit()
    conn.close()

    return {"message": "Upgraded to Pro"}
