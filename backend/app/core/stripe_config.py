import stripe

STRIPE_SECRET_KEY = "sk_test_your_key_here"
STRIPE_WEBHOOK_SECRET = "whsec_your_webhook_secret_here"

stripe.api_key = STRIPE_SECRET_KEY

PRICE_ID = "price_your_price_id_here"
