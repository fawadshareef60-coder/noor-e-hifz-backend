from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models_recordings import Recording
from app.schemas import RecordingCreate, RecordingResponse
from app.auth import get_current_user

router = APIRouter(
    prefix="/recordings",
    tags=["Audio Submission Engine"]
)

# ==========================================
# 1. LOG NEW AUDIO RECORDING SUBMISSION
# ==========================================
@router.post("/submit", response_model=RecordingResponse, status_code=status.HTTP_201_CREATED)
def submit_audio_recording(
    recording_data: RecordingCreate, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    """
    Student ki live tilawat ya recitation audio file ka path aur meta details database mein log karta hai.
    """
    if recording_data.lesson_type not in ["sabaq", "sabqi", "manzil"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Ghalat lesson_type! Yeh sirf 'sabaq', 'sabqi' ya 'manzil' ho sakta hai."
        )
        
    new_recording = Recording(
        student_id=current_user["id"],
        lesson_type=recording_data.lesson_type,
        audio_url=recording_data.audio_url,
        format=recording_data.format,
        duration_seconds=recording_data.duration_seconds
    )
    
    db.add(new_recording)
    db.commit()
    db.refresh(new_recording)
    return new_recording

# ==========================================
# 2. FETCH SPECIFIC RECORDING BY ID
# ==========================================
@router.get("/{recording_id}", response_model=RecordingResponse)
def get_recording_details(
    recording_id: str, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    """
    Recording ID ke mutabiq student ki audio file ka details aur static server cloud storage URL fetch karta hai.
    """
    recording = db.query(Recording).filter(Recording.id == recording_id).first()
    
    if not recording:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Mataluba recording file ka record nahi mila."
        )
        
    # Check if student is accessing their own recording or user is admin
    if recording.student_id != current_user["id"] and current_user["role"] != "administrator":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Aapko is audio record ko dekhne ki ijazat nahi hai."
        )
        
    return recording
