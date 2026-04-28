from fastapi import HTTPException, Header
from jose import jwt, JWTError

import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
ALGORITHM = "HS256"

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    try:
        scheme, token = authorization.split()

        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid auth scheme")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user = payload.get("sub")
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        return user

    except (JWTError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid or expired token")
