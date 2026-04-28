import stripe
from fastapi import Request, APIRouter

from backend.app.core.stripe_config import STRIPE_WEBHOOK_SECRET
from backend.app.db.database import get_connection

router = APIRouter()

@router.post("/stripe-webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig, STRIPE_WEBHOOK_SECRET
        )
    except:
        return {"error": "Invalid webhook"}

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        email = session["customer_email"]

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE users SET plan='pro' WHERE email=?",
            (email,)
        )

        conn.commit()
        conn.close()

    return {"status": "ok"}
