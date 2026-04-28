from fastapi import FastAPI
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
from backend import ai, auth
from backend.db import init_db
from backend.admin_routes import router as admin_router
from backend.billing import router as billing_router

app = FastAPI(title="SEO SaaS AI Engine")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init DB
init_db()

# routes
app.include_router(ai.router)
app.include_router(auth.router)
app.include_router(admin_router)
app.include_router(billing_router)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}
