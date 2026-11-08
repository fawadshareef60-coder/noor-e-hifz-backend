from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models_support import Guardian, Notification, AuditLog
from app.auth import get_current_user

router = APIRouter(
    prefix="/support",
    tags=["Parental Supervision & System Operations"]
)

# ==========================================
# 1. REGISTER GUARDIAN / PARENT CONNECTION
# ==========================================
@router.post("/guardian/connect", status_code=status.HTTP_201_CREATED)
def connect_guardian_profile(
    student_id: str,
    guardian_name: str,
    guardian_contact: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Bachon ke account par parental control settings apply karne ke liye Guardian link karta hai.
    """
    if current_user["role"] != "administrator" and current_user["id"] != student_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Aapko is student ke sath guardian details link karne ki ijazat nahi hai."
        )

    new_guardian = Guardian(
        student_id=student_id,
        guardian_name=guardian_name,
        guardian_contact=guardian_contact,
        consent_granted=True
    )
    db.add(new_guardian)
    db.commit()
    return {"message": "Parent/Guardian connection successfully configure ho gaya hai."}

# ==========================================
# 2. FETCH UNREAD NOTIFICATIONS / ALERTS
# ==========================================
@router.get("/notifications/unread", response_model=List[dict])
def get_unread_notifications(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Student ya Admin dashboard ke liye real-time unread sabaq reminders aur revision alerts laata hai.
    """
    notifications = db.query(Notification).filter(
        Notification.user_id == current_user["id"],
        Notification.is_read == False
    ).order_by(Notification.created_at.desc()).all()

    return [
        {
            "id": str(n.id),
            "title": n.title,
            "message": n.message,
            "created_at": str(n.created_at)
        }
        for n in notifications
    ]

# ==========================================
# 3. LOG SYSTEM SECURITY EVENT (AUDIT)
# ==========================================
@router.post("/audit/log", status_code=status.HTTP_201_CREATED)
def trigger_security_audit_log(
    request: Request,
    action: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    System ke sensitive actions (jaise password change ya settings alteration) ko secure IP logs ke sath audit trail mein record karta hai.
    """
    client_ip = request.client.host if request.client else "Unknown IP"
    
    new_log = AuditLog(
        user_id=current_user["id"],
        action_performed=action,
        ip_address=client_ip
    )
    db.add(new_log)
    db.commit()
    return {"status": "Audit event recorded successfully."}
