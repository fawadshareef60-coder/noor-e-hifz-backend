from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date, datetime, timezone
from app.database import get_db
from app.models_lessons import SabaqLesson, SabqiLesson, ManzilLesson
from app.auth import get_current_user

router = APIRouter(
    prefix="/lessons",
    tags=["Madrasa Lesson Tracking Engine"]
)

# ==========================================
# 1. ASSIGN NEW SABAQ (DAILY LESSON)
# ==========================================
@router.post("/sabaq/assign", status_code=status.HTTP_201_CREATED)
def assign_sabaq(student_id: str, start_ayah_id: str, end_ayah_id: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Sirf Admin ya System student ko daily ka naya Sabaq range assign kar sakta hai.
    """
    if current_user["role"] != "administrator":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Sarf admin naya sabaq assign kar sakta hai.")
        
    new_sabaq = SabaqLesson(
        student_id=student_id,
        start_ayah_id=start_ayah_id,
        end_ayah_id=end_ayah_id,
        status="pending"
    )
    db.add(new_sabaq)
    db.commit()
    return {"message": "Sabaq successfully assign ho gaya hai."}

# ==========================================
# 2. FETCH STUDENT ACTIVE LESSONS
# ==========================================
@router.get("/today")
def get_today_lessons(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Student ke login token ke mutabiq uska aaj ka Sabaq, Sabqi aur Manzil fetch karta hai.
    """
    sabaq = db.query(SabaqLesson).filter(SabaqLesson.student_id == current_user["id"], SabaqLesson.status != "completed").first()
    sabqi = db.query(SabqiLesson).filter(SabqiLesson.student_id == current_user["id"]).first()
    manzil = db.query(ManzilLesson).filter(ManzilLesson.student_id == current_user["id"]).first()
    
    return {
        "sabaq": {"start": sabaq.start_ayah_id, "end": sabaq.end_ayah_id, "status": sabaq.status} if sabaq else None,
        "sabqi": {"start": sabqi.start_ayah_id, "end": sabqi.end_ayah_id, "status": sabqi.status} if sabqi else None,
        "manzil": {"start": manzil.start_ayah_id, "end": manzil.end_ayah_id, "status": manzil.status} if manzil else None
    }

# ==========================================
# 3. UPDATE SABAQ STATUS TO COMPLETED
# ==========================================
@router.patch("/sabaq/{lesson_id}/complete")
def complete_sabaq(lesson_id: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Student jab recitation complete kar leta hai toh sabaq ka status update ho jata hai.
    """
    lesson = db.query(SabaqLesson).filter(SabaqLesson.id == lesson_id, SabaqLesson.student_id == current_user["id"]).first()
    if not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson record nahi mila.")
        
    lesson.status = "completed"
    lesson.completed_date = date.today()
    db.commit()
    return {"message": "Alhamdulillah, sabaq complete mark ho gaya."}
