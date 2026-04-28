from fastapi import APIRouter, Depends
from backend.app.core.admin import get_admin_user
from backend.app.db.database import get_connection

router = APIRouter(prefix="/admin", tags=["Admin"])

# 🔹 List all users
@router.get("/users")
def list_users(admin: str = Depends(get_admin_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT email, plan, is_admin FROM users")
    users = cur.fetchall()
    conn.close()

    return {"users": [dict(u) for u in users]}


# 🔹 Upgrade user
@router.post("/upgrade")
def upgrade_user(email: str, admin: str = Depends(get_admin_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("UPDATE users SET plan='pro' WHERE email=?", (email,))
    conn.commit()
    conn.close()

    return {"message": f"{email} upgraded to Pro"}


# 🔹 Downgrade user
@router.post("/downgrade")
def downgrade_user(email: str, admin: str = Depends(get_admin_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("UPDATE users SET plan='free' WHERE email=?", (email,))
    conn.commit()
    conn.close()

    return {"message": f"{email} downgraded to Free"}


# 🔹 View usage per user
@router.get("/usage")
def usage(admin: str = Depends(get_admin_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT user_email, COUNT(*) as total
        FROM usage_logs
        GROUP BY user_email
    """)

    data = cur.fetchall()
    conn.close()

    return {"usage": [dict(row) for row in data]}
