from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from app.database import Base

# ==========================================
# AUDIO RECORDINGS LOGGING MODEL
# ==========================================
class Recording(Base):
    __tablename__ = "recordings"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    lesson_type = Column(String(50), nullable=False) # 'sabaq', 'sabqi', ya 'manzil'
    audio_url = Column(Text, nullable=False)         # Supabase/S3 Cloud Storage secure file path link
    format = Column(String(10), default="wav")       # e.g., 'wav', 'm4a', 'mp3'
    duration_seconds = Column(Integer, nullable=False)
    submitted_at = Column(DateTime(timezone=True), server_default=sa.func.now())

    # Bi-directional relationship tracking for analytics mapping
    student = relationship("User", back_populates="recordings")
