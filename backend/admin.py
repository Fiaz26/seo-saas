from backend.db import SessionLocal
from backend.models import User


def upgrade_user_plan(username: str, plan: str):
    db = SessionLocal()

    user = db.query(User).filter(User.username == username).first()

    if not user:
        db.close()
        return {"error": "user not found"}

    user.plan = plan

    db.commit()
    db.close()

    return {
        "message": f"User upgraded to {plan}",
        "username": username
    }
