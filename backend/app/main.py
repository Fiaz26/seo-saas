from fastapi import FastAPI

from backend.app.api.ai.routes import router as ai_router
from backend.app.api.auth.routes import router as auth_router
from backend.app.api.dashboard.routes import router as dashboard_router
from backend.app.api.billing.routes import router as billing_router
from backend.app.api.admin.routes import router as admin_router
from backend.app.db.database import init_db

app = FastAPI(title="SEO SaaS Platform")

init_db()

@app.get("/")
def home():
    return {"status": "SaaS backend running"}

app.include_router(auth_router)
app.include_router(ai_router)
app.include_router(dashboard_router)
app.include_router(billing_router)
app.include_router(admin_router)
