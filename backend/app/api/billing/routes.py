from fastapi import APIRouter

router = APIRouter(prefix="/billing", tags=["Billing"])

@router.get("/upgrade-info")
def upgrade_info():
    return {
        "message": "Send payment via Payoneer",
        "method": "Bank Transfer / Payoneer",
        "instructions": "After payment, send screenshot to support",
        "email": "your-payoneer-email@example.com"
    }
