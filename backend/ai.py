from fastapi import APIRouter, Depends
from backend.security_api import verify_api_key
from backend import ai_service, keywords
from backend.storage import save_project

router = APIRouter(prefix="/ai", tags=["AI Tools"])


@router.get("/blog")
def blog(topic: str, user: str = Depends(verify_api_key)):
    result = ai_service.generate_blog(topic)

    save_project(topic, str(result), "")

    return {"user": user, "data": result}


@router.get("/keywords")
def keywords_api(topic: str, user: str = Depends(verify_api_key)):
    return {"user": user, "data": keywords.generate_keywords(topic)}


@router.get("/projects")
def projects(user: str = Depends(verify_api_key)):
    return {"user": user, "data": "protected projects data"}
