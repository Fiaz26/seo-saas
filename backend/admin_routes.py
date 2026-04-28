from fastapi import APIRouter, Depends
from backend.admin import upgrade_user_plan
from backend.admin_security import verify_admin
from backend.db import SessionLocal
from backend.models import APIKey

router = APIRouter(prefix="/admin", tags=["Admin Panel"])


@router.post("/upgrade-user")
def upgrade_user(username: str, plan: str, admin=Depends(verify_admin)):
    return upgrade_user_plan(username, plan)


@router.post("/reset-usage")
def reset_usage(username: str, admin=Depends(verify_admin)):
    db = SessionLocal()

    keys = db.query(APIKey).filter(APIKey.username == username).all()

    for k in keys:
        k.usage = 0

    db.commit()
    db.close()

    return {"message": "usage reset", "user": username}


from backend.models import APIKey

@router.get("/analytics")
def analytics(admin=Depends(verify_admin)):
    db = SessionLocal()

    keys = db.query(APIKey).all()

    total_usage = sum(k.usage for k in keys)

    data = [
        {"username": k.username, "usage": k.usage}
        for k in keys
    ]

    db.close()

    return {
        "total_usage": total_usage,
        "users": data
    }


@router.get("/billing-requests")
def get_requests(admin=Depends(verify_admin)):
    db = SessionLocal()
    reqs = db.query(BillingRequest).all()
    db.close()

    return [
        {
            "id": r.id,
            "username": r.username,
            "plan": r.plan,
            "status": r.status
        }
        for r in reqs
    ]


@router.post("/approve-request")
def approve_request(request_id: int, admin=Depends(verify_admin)):
    db = SessionLocal()

    req = db.query(BillingRequest).filter(BillingRequest.id == request_id).first()

    if not req:
        return {"error": "Not found"}

    user = db.query(User).filter(User.username == req.username).first()
    user.plan = req.plan

    req.status = "approved"

    db.commit()
    db.close()

    return {"message": "approved"}
