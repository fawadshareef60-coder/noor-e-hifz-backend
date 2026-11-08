from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
import sqlalchemy as sa
from app.database import Base

# ==========================================
# 1. GUARDIAN / PARENTAL CONTROL MODEL
# ==========================================
class Guardian(Base):
    __tablename__ = "guardians"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    student_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    guardian_name = Column(String(255), nullable=False)
    guardian_contact = Column(String(100), nullable=False)
    consent_granted = Column(Boolean, default=False)
    account_controls = Column(JSONB, default=dict) # Stores screen boundaries or weekly target parameters
    created_at = Column(DateTime(timezone=True), server_default=sa.func.now())

# ==========================================
# 2. REAL-TIME SYSTEM NOTIFICATIONS MODEL
# ==========================================
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    user_id = Column(String(36), ForeignKey("users.id", on_delete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=sa.func.now())

# ==========================================
# 3. SECURITY AUDIT LOGGING MODEL
# ==========================================
class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String(36), primary_key=True, server_default=sa.text("uuid_generate_v4()"))
    user_id = Column(String(36), ForeignKey("users.id", on_delete="SET NULL"), nullable=True, index=True)
    action_performed = Column(Text, nullable=False) # Logs actions like password resets or critical level changes
    ip_address = Column(String(50), nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=sa.func.now())
