from fastapi import APIRouter, Depends
from backend.db import get_db
from backend.models import BillingRequest

router = APIRouter(prefix="/billing", tags=["Billing"])

@router.post("/request-upgrade")
def request_upgrade(username: str, plan: str, db=Depends(get_db)):

    req = BillingRequest(
        username=username,
        plan=plan,
        status="pending"
    )

    db.add(req)
    db.commit()

    return {"message": "Request saved", "status": "pending"}
