from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any, List
from datetime import datetime, date

# ==========================================
# USER & PROFILE SCHEMAS
# ==========================================

class UserBase(BaseModel):
    email: EmailStr
    phone_number: Optional[str] = None
    role: str = "student"

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")

class UserResponse(UserBase):
    id: Any
    created_at: datetime

    class Config:
        from_attributes = True

class ProfileCreate(BaseModel):
    full_name: str
    age: int = Field(..., ge=4, le=100, description="Age must be between 4 and 100")
    preferred_language: Optional[str] = "Urdu"
    country: Optional[str] = None
    time_zone: Optional[str] = None
    educational_background: Optional[str] = None
    quran_reading_proficiency: Optional[str] = "Beginner"
    existing_memorization: Optional[str] = None
    tajweed_knowledge: Optional[str] = None
    available_daily_study_time: Optional[int] = 30 # minutes
    preferred_study_schedule: Optional[Dict[str, Any]] = None
    current_level: Optional[str] = "Level 1: Beginner Reading"

class ProfileResponse(ProfileCreate):
    id: Any
    updated_at: datetime

    class Config:
        from_attributes = True

# ==========================================
# AUDIO RECORDING SCHEMAS
# ==========================================

class RecordingCreate(BaseModel):
    lesson_type: str = Field(..., description="Must be 'sabaq', 'sabqi', or 'manzil'")
    audio_url: str
    format: str = "wav"
    duration_seconds: int

class RecordingResponse(BaseModel):
    id: Any
    student_id: Any
    lesson_type: str
    audio_url: str
    format: str
    duration_seconds: int
    submitted_at: datetime

    class Config:
        from_attributes = True

# ==========================================
# AI ASSESSMENT & MISTAKE SCHEMAS
# ==========================================

class MistakeRecordSchema(BaseModel):
    ayah_id: Any
    error_type: str # 'text_accuracy', 'pronunciation', 'tajweed', 'fluency'
    word_index: int
    detected_mistake: Optional[str] = None
    suggested_correction: str
    audio_timestamp_start: Optional[float] = None
    audio_timestamp_end: Optional[float] = None

class AIAssessmentResponse(BaseModel):
    id: Any
    recording_id: Any
    recognized_transcript: Optional[str] = None
    confidence_level: float
    is_low_confidence: bool
    created_at: datetime
    mistakes: List[MistakeRecordSchema] = []

    class Config:
        from_attributes = True
