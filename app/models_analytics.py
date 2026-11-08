from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey, Numeric
import sqlalchemy as sa
from app.database import Base

# ==========================================
# 1. SPACED REPITITION REVISION SCHEDULE MODEL
# ==========================================
class RevisionSchedule(Base):
    __tablename__ = "revision_schedules"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    ayah_id = Column(String(36), ForeignKey("quran_ayahs.id"), nullable=False)
    scheduled_date = Column(Date, nullable=False, index=True)
    priority = Column(String(20), default="medium") # 'high' for repeated mistakes, 'medium', 'low'
    is_done = Column(Boolean, default=False)

# ==========================================
# 2. STUDY SESSION TRACKING MODEL (Daily Time Spent)
# ==========================================
class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    activity_type = Column(String(50), nullable=False) # 'sabaq', 'sabqi', 'manzil', 'tajweed', 'tafseer'
    duration_minutes = Column(Integer, nullable=False)
    session_date = Column(Date, server_default=sa.func.current_date())

# ==========================================
# 3. CONSOLIDATED PROGRESS SNAPSHOT MODEL
# ==========================================
class ProgressRecord(Base):
    __tablename__ = "progress_records"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, unique=True)
    total_paras_memorized = Column(Integer, default=0)
    total_surahs_completed = Column(Integer, default=0)
    total_ayahs_memorized = Column(Integer, default=0)
    revision_accuracy = Column(Numeric(5, 2), default=100.00) # Global accuracy scale
