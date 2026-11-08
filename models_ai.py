from sqlalchemy import Column, String, Integer, Numeric, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from app.database import Base

# ==========================================
# 1. CORE AI ASSESSMENT OVERVIEW MODEL
# ==========================================
class AIAssessment(Base):
    __tablename__ = "ai_assessments"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    recording_id = Column(String(36), ForeignKey("recordings.id", on_delete="CASCADE"), nullable=False, index=True)
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    recognized_transcript = Column(Text, nullable=True) # Speech-to-text text representation
    confidence_level = Column(Numeric(5, 2), nullable=False) # e.g., 96.50%
    is_low_confidence = Column(Boolean, default=False)
    assessment_limitations = Column(Text, nullable=True) # Noise or background issues logs
    created_at = Column(DateTime(timezone=True), server_default=sa.func.now())

    # Relationships
    mistakes = relationship("MistakeRecord", back_populates="assessment", cascade="all, delete-orphan")

# ==========================================
# 2. GRANULAR MISTAKE ANALYSIS MODEL
# ==========================================
class MistakeRecord(Base):
    __tablename__ = "mistake_records"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    assessment_id = Column(String(36), ForeignKey("ai_assessments.id", on_delete="CASCADE"), nullable=False, index=True)
    ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    error_type = Column(String(50), nullable=False) # 'text_accuracy', 'pronunciation', 'tajweed', 'fluency'
    word_index = Column(Integer, nullable=False)     # Position of the specific word in the Ayah
    detected_mistake = Column(String(255), nullable=True)
    suggested_correction = Column(Text, nullable=False)
    audio_timestamp_start = Column(Numeric(6, 2), nullable=True) # Exact seconds when error started
    audio_timestamp_end = Column(Numeric(6, 2), nullable=True)   # Exact seconds when error ended

    # Relationships
    assessment = relationship("AIAssessment", back_populates="mistakes")
