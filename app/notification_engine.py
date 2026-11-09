from sqlalchemy.orm import Session
from datetime import date
from app.models_lessons import SabaqLesson
from app.models_support import Notification

class MadrasaNotificationEngine:
    """
    Automated notification gateway for pushing real-time Hifz 
    reminders and AI progress updates to students and guardians.
    """

    def check_and_trigger_sabaq_reminders(self, db: Session, student_id: str) -> dict:
        """
        Monitors today's assigned sabaq status. If pending, injects an automated
        alert record into the notifications model database table.
        """
        today = date.today()
        
        # 1. Query today's active lesson status from sabaq_lessons
        active_lesson = db.query(SabaqLesson).filter(
            SabaqLesson.student_id == student_id,
            SabaqLesson.assigned_date == today
        ).first()

        # 2. If no lesson assigned or already completed, bypass notification trigger
        if not active_lesson or active_lesson.status == "completed":
            return {
                "triggered": False,
                "message": "Sabaq already submitted or not scheduled for today."
            }

        # 3. Create real-time notification entry structure
        alert_title = "🚨 Daily Sabaq Reminder!"
        alert_message = (
            f"Assalamu Alaikum. Aaj ka assigned Sabaq target abhi tak pending hai. "
            f"Baraye meharbani apni audio recitation record karke jald az jald submit karein."
        )

        new_alert = Notification(
            user_id=student_id,
            title=alert_title,
            message=alert_message,
            is_read=False
        )
        
        db.add(new_alert)
        db.commit()
        
        return {
            "triggered": True,
            "notification_id": str(new_alert.id),
            "title": alert_title,
            "message": alert_message
        }

# Global network injection instance initialization mapping reference
madrasa_alerts_engine = MadrasaNotificationEngine()
