from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def dashboard_home():
    return {
        "project": "SEO SaaS",
        "status": "active",
        "features": [
            "AI Blog Generator",
            "SEO Engine",
            "Automation Ready"
        ]
    }
