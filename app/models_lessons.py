from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from app.database import Base

# ==========================================
# 1. DAILY SABAQ TRACKING MODEL (New Lesson)
# ==========================================
class SabaqLesson(Base):
    __tablename__ = "sabaq_lessons"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    start_ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    end_ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    status = Column(String(30), default="pending") # 'pending', 'in_progress', 'completed', 'needs_revision'
    assigned_date = Column(Date, server_default=sa.func.current_date())
    completed_date = Column(Date, nullable=True)

# ==========================================
# 2. SABQI TRACKING MODEL (Recent Back-Revision)
# ==========================================
class SabqiLesson(Base):
    __tablename__ = "sabqi_lessons"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    start_ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    end_ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    status = Column(String(30), default="pending")
    revision_count = Column(Integer, default=0) # Kitni baar yeh sabqi dohrai gayi
    last_reviewed_at = Column(DateTime(timezone=True), nullable=True)

# ==========================================
# 3. MANZIL TRACKING MODEL (Large Quarter/Juz Revision)
# ==========================================
class ManzilLesson(Base):
    __tablename__ = "manzil_lessons"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    start_ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    end_ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    status = Column(String(30), default="pending")
    last_reviewed_at = Column(DateTime(timezone=True), nullable=True)
