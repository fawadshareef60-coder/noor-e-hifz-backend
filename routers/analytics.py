from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date, timedelta
from typing import List
from app.database import get_db
from app.models_analytics import RevisionSchedule, StudySession, ProgressRecord
from app.auth import get_current_user

router = APIRouter(
    prefix="/analytics",
    tags=["Smart Revision & Analytics Engine"]
)

# ==========================================
# 1. FETCH TODAY'S AUTOMATED REVISION PLAN
# ==========================================
@router.get("/revision-plan", response_model=List[dict])
def get_daily_revision_plan(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Spaced Repetition ke mutabiq student ki weak Ayahs aur scheduled revisions ki list laata hai.
    """
    today = date.today()
    plan = db.query(RevisionSchedule).filter(
        RevisionSchedule.student_id == current_user["id"],
        RevisionSchedule.scheduled_date <= today,
        RevisionSchedule.is_done == False
    ).order_by(RevisionSchedule.priority.desc()).all()
    
    return [
        {
            "id": str(r.id),
            "ayah_id": str(r.ayah_id),
            "scheduled_date": str(r.scheduled_date),
            "priority": r.priority
        }
        for r in plan
    ]

# ==========================================
# 2. LOG STUDY SESSION TIME
# ==========================================
@router.post("/log-session", status_code=status.HTTP_201_CREATED)
def log_study_time(
    activity_type: str, 
    duration_minutes: int, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    """
    Student ne kis activity (Sabaq, Sabqi, Manzil, Tajweed) par kitna waqt guzara, yeh record karta hai.
    """
    if activity_type not in ["sabaq", "sabqi", "manzil", "tajweed", "tafseer"]:
        raise HTTPException(status_code=400, detail="Ghalat activity type format.")
        
    new_session = StudySession(
        student_id=current_user["id"],
        activity_type=activity_type,
        duration_minutes=duration_minutes
    )
    db.add(new_session)
    db.commit()
    return {"message": "Study session successfully log ho gaya."}

# ==========================================
# 3. GET GLOBAL PROGRESS SNAPSHOT
# ==========================================
@router.get("/progress-snapshot")
def get_progress_snapshot(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Student dashboard ke liye total memorized content aur live accuracy ratios fetch karta hai.
    """
    progress = db.query(ProgressRecord).filter(ProgressRecord.student_id == current_user["id"]).first()
    if not progress:
        return {
            "total_paras_memorized": 0,
            "total_surahs_completed": 0,
            "total_ayahs_memorized": 0,
            "revision_accuracy": 100.00
        }
        
    return {
        "total_paras_memorized": progress.total_paras_memorized,
        "total_surahs_completed": progress.total_surahs_completed,
        "total_ayahs_memorized": progress.total_ayahs_memorized,
        "revision_accuracy": float(progress.revision_accuracy)
    }
