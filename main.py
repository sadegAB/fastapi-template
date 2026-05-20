from fastapi import FastAPI

from config import settings
from middleware.cors import add_cors
from routers import health

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
)

add_cors(app)

app.include_router(health.router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": f"Welcome to {settings.app_name}",
        "docs": "/docs",
        "health": "/health/",
    }
