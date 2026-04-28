from fastapi import APIRouter, Depends
from backend.app.core.security import get_current_user
from backend.app.db.database import get_connection

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/usage")
def get_usage(user_email: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) as total FROM usage_logs WHERE user_email=?", (user_email,))
    total = cur.fetchone()["total"]

    conn.close()

    return {"user": user_email, "total_requests": total}


@router.get("/history")
def get_history(user_email: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT endpoint, timestamp FROM usage_logs
        WHERE user_email=?
        ORDER BY id DESC LIMIT 20
    """, (user_email,))

    rows = cur.fetchall()
    conn.close()

    return {"history": [dict(r) for r in rows]}


@router.get("/stats")
def get_stats(user_email: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) as total FROM usage_logs WHERE user_email=?", (user_email,))
    total = cur.fetchone()["total"]

    conn.close()

    return {"user": user_email, "total_requests": total}
