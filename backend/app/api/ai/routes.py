from fastapi import APIRouter, Depends
from backend.app.middleware.usage import log_usage, check_limit
from backend.app.core.security import get_current_user

router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/keywords")
def generate_keywords(topic: str, user_email: str = Depends(get_current_user)):

    if not check_limit(user_email):
        return {"error": "Daily limit reached. Upgrade to Pro."}

    log_usage(user_email, "/ai/keywords")

    return {
        "user": user_email,
        "topic": topic,
        "keywords": [
            f"{topic} tips",
            f"{topic} strategy",
            f"best {topic} tools"
        ]
    }
