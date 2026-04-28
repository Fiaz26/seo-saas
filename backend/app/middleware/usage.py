from backend.app.db.database import get_connection
from backend.app.core.plans import get_user_plan, FREE_LIMIT
from datetime import datetime

def log_usage(user_email: str, endpoint: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO usage_logs (user_email, endpoint, timestamp)
        VALUES (?, ?, ?)
    """, (user_email, endpoint, str(datetime.utcnow())))

    conn.commit()
    conn.close()

def check_limit(user_email: str):
    plan = get_user_plan(user_email)

    if plan == "pro":
        return True

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*) as total FROM usage_logs
        WHERE user_email=?
    """, (user_email,))

    total = cur.fetchone()["total"]
    conn.close()

    return total < FREE_LIMIT
