from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models_ai import AIAssessment, MistakeRecord
from app.schemas import AIAssessmentResponse, MistakeRecordSchema
from app.auth import get_current_user

router = APIRouter(
    prefix="/assessments",
    tags=["AI Evaluation Engine"]
)

# ==========================================
# 1. SAVE AI MODEL EVALUATION DATA
# ==========================================
@router.post("/log-result", status_code=status.HTTP_201_CREATED)
def log_ai_assessment_result(
    recording_id: str,
    student_id: str,
    confidence_level: float,
    recognized_transcript: str = None,
    is_low_confidence: bool = False,
    mistakes: List[MistakeRecordSchema] = [],
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Core AI engine jab recording verify kar leta hai, toh yeh route transcript, 
    accuracy confidence level, aur tilawat ki mistakes ko automatically save karta hai.
    """
    # Only System/Admin or authorized AI agent role can trigger this result generation
    if current_user["role"] != "administrator":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Sirf system automated processes ya admin hi AI evaluation logs submit kar sakte hain."
        )

    # Insert overview assessment records
    new_assessment = AIAssessment(
        recording_id=recording_id,
        student_id=student_id,
        recognized_transcript=recognized_transcript,
        confidence_level=confidence_level,
        is_low_confidence=is_low_confidence
    )
    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)

    # Insert individual error records if any mistake detected
    for mistake in mistakes:
        new_mistake = MistakeRecord(
            assessment_id=new_assessment.id,
            ayah_id=mistake.ayah_id,
            error_type=mistake.error_type,
            word_index=mistake.word_index,
            detected_mistake=mistake.detected_mistake,
            suggested_correction=mistake.suggested_correction,
            audio_timestamp_start=mistake.audio_timestamp_start,
            audio_timestamp_end=mistake.audio_timestamp_end
        )
        db.add(new_mistake)
    
    db.commit()
    return {"message": "AI assessment aur logs kamyabi se save ho gaye hain.", "assessment_id": str(new_assessment.id)}

# ==========================================
# 2. FETCH STUDENT REPORT BY RECORDING ID
# ==========================================
@router.get("/report/{recording_id}", response_model=AIAssessmentResponse)
def get_ai_report_by_recording(
    recording_id: str, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    """
    Student ya Teacher ke dashboard ke liye specific recording ka granular AI fault analysis fetch karta hai.
    """
    assessment = db.query(AIAssessment).filter(AIAssessment.recording_id == recording_id).first()
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Is recording ka AI analysis report abhi tak generate nahi hua."
        )

    # Security check: User can only see their own reports unless admin
    if assessment.student_id != current_user["id"] and current_user["role"] != "administrator":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Aapko is evaluation audit sheet ko dekhne ki ijazat nahi hai."
        )

    return assessment
