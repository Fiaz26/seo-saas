from backend.app.db.database import get_connection

FREE_LIMIT = 20

def get_user_plan(email: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT plan FROM users WHERE email=?", (email,))
    user = cur.fetchone()

    conn.close()

    if not user:
        return "free"

    return user["plan"]

def is_pro(email: str):
    return get_user_plan(email) == "pro"
