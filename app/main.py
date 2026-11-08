from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

# Core Configuration & Connection Managers
from config import settings
from database import get_db, engine, Base

# Import all developed routers from pipeline modules
from routers import auth, profiles, quran, lessons, recordings, ai_assessments, analytics, support

# Automatic database tables generation sequence
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-Powered Digital Madrasa System for Advanced Hifz & Tajweed Management Tracking Engine.",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Security Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router Integration Injection Pipeline
app.include_router(auth.router, prefix=settings.API_STR)
app.include_router(profiles.router, prefix=settings.API_STR)
app.include_router(quran.router, prefix=settings.API_STR)
app.include_router(lessons.router, prefix=settings.API_STR)
app.include_router(recordings.router, prefix=settings.API_STR)
app.include_router(ai_assessments.router, prefix=settings.API_STR)
app.include_router(analytics.router, prefix=settings.API_STR)
app.include_router(support.router, prefix=settings.API_STR)

@app.get("/", tags=["System Root Routing"])
def root_status_check():
    return {
        "project": settings.PROJECT_NAME,
        "status": "online",
        "api_version": settings.VERSION,
        "engine": "FastAPI ASGI Server Wrapper"
    }

@app.get("/health", tags=["System Root Routing"])
def live_database_health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database_connectivity": "connected",
            "message": "All pipeline networks operational."
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database_connectivity": "disconnected",
            "system_exception": str(e)
        }
