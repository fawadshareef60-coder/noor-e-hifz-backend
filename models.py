from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric, Text, DateTime, Date, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from app.database import Base

# ==========================================
# 1. CORE USER MANAGEMENT MODELS
# ==========================================

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone_number = Column(String(50), unique=True, nullable=True)
    role = Column(String(50), default="student", nullable=False)
    hashed_password = Column(String(255), nullable=False) # Secure encrypted password
    created_at = Column(DateTime(timezone=True), server_default=sa.func.now())
    updated_at = Column(DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now())

    # Bi-directional Relationship mappings
    profile = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUID(as_uuid=True), ForeignKey("users.id", on_delete="CASCADE"), primary_key=True)
    full_name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    preferred_language = Column(String(50), default="Urdu")
    country = Column(String(100), nullable=True)
    time_zone = Column(String(100), nullable=True)
    educational_background = Column(Text, nullable=True)
    quran_reading_proficiency = Column(String(100), nullable=True)
    existing_memorization = Column(Text, nullable=True)
    tajweed_knowledge = Column(Text, nullable=True)
    available_daily_study_time = Column(Integer, default=30)
    current_level = Column(String(100), default="Level 1: Beginner Reading")
    created_at = Column(DateTime(timezone=True), server_default=sa.func.now())
    updated_at = Column(DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now())

    user = relationship("User", back_populates="profile")

