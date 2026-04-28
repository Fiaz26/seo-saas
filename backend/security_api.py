from fastapi import Header, HTTPException
from backend.db import SessionLocal
from backend.models import APIKey, User
from backend.limits import check_limit

def verify_api_key(x_api_key: str = Header(...)):
    db = SessionLocal()

    # 1. Find API key
    key = db.query(APIKey).filter(APIKey.key == x_api_key).first()
    if not key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # 2. Find user (THIS FIXES YOUR ERROR)
    user = db.query(User).filter(User.username == key.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 3. Check limit
    if not check_limit(user.plan, key.usage):
        raise HTTPException(status_code=403, detail="Usage limit reached")

    # 4. Increase usage
    key.usage += 1
    db.commit()

    return user.username
