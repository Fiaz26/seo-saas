from fastapi import Depends, HTTPException
from backend.app.core.security import get_current_user
from backend.app.db.database import get_connection

def get_admin_user(user_email: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT is_admin FROM users WHERE email=?", (user_email,))
    user = cur.fetchone()
    conn.close()

    if not user or user["is_admin"] != 1:
        raise HTTPException(status_code=403, detail="Admin access required")

    return user_email
