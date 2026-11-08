from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Profile, User
from app.schemas import ProfileCreate, ProfileResponse
from app.auth import get_current_user

router = APIRouter(
    prefix="/profiles",
    tags=["Student Profile Management"]
)

# ==========================================
# 1. CREATE / SETUP PROFILE
# ==========================================
@router.post("/setup", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
def setup_student_profile(
    profile_data: ProfileCreate, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    """
    Login shuda student ki detailed profile database mein setup karta hai.
    """
    # Check if profile already exists for the logged in user
    existing_profile = db.query(Profile).filter(Profile.id == current_user["id"]).first()
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Aapki profile pehle se setup hai. Update endpoint use karein."
        )
    
    # Create new profile entry tied to user UUID
    new_profile = Profile(
        id=current_user["id"],
        full_name=profile_data.full_name,
        age=profile_data.age,
        preferred_language=profile_data.preferred_language,
        country=profile_data.country,
        time_zone=profile_data.time_zone,
        educational_background=profile_data.educational_background,
        quran_reading_proficiency=profile_data.quran_reading_proficiency,
        existing_memorization=profile_data.existing_memorization,
        tajweed_knowledge=profile_data.tajweed_knowledge,
        available_daily_study_time=profile_data.available_daily_study_time,
        current_level=profile_data.current_level
    )
    
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

# ==========================================
# 2. FETCH CURRENT STUDENT PROFILE
# ==========================================
@router.get("/me", response_model=ProfileResponse)
def get_my_profile(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Active user token ke mutabiq database se student ki live details fetch karta hai.
    """
    profile = db.query(Profile).filter(Profile.id == current_user["id"]).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_444_NOT_FOUND,
            detail="Profile nahi mili. Pehle profile setup mukammal karein."
        )
    return profile

# ==========================================
# 3. UPDATE HIFZ PLACEMENT LEVEL (ADMIN ONLY)
# ==========================================
@router.patch("/{student_id}/update-level", response_model=ProfileResponse)
def update_student_placement_level(
    student_id: str, 
    new_level: str, 
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)
):
    """
    Sirf platform Administrators students ka Hifz level (Level 1 se Level 6) tabdeel kar sakte hain.
    """
    if current_user["role"] != "administrator":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sarf Administrators ke paas yeh level change karne ki ijazat hai."
        )
        
    profile = db.query(Profile).filter(Profile.id == student_id).first()
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_444_NOT_FOUND,
            detail="Mataluba student ki profile nahi mili."
        )
        
    profile.current_level = new_level
    db.commit()
    db.refresh(profile)
    return profile
