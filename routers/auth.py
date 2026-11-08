from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Profile
from app.schemas import UserCreate, UserResponse, ProfileCreate, ProfileResponse
from app.auth import get_password_hash, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication Engine"]
)

# ==========================================
# 1. STUDENT REGISTRATION ENDPOINT
# ==========================================
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_student(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Naya student account create karne ke liye:
    Email uniqueness verify karta hai aur password ko hash karke save karta hai.
    """
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Yeh email address pehle se register hai."
        )
    
    # Hash password safely
    hashed_pwd = get_password_hash(user_data.password)
    
    # Create database entry
    new_user = User(
        email=user_data.email,
        phone_number=user_data.phone_number,
        role=user_data.role,
        hashed_password=hashed_pwd
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ==========================================
# 2. LOGIN / TOKEN GENERATION ENDPOINT
# ==========================================
@router.post("/login")
def login_student(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Student login credentials verify karta hai aur secure active session token return karta hai.
    """
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ghalat email ya password. Dobara koshish karein.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generate active session JWT token
    access_token = create_access_token(
        data={"sub": user.email, "id": str(user.id), "role": user.role}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
        "user_id": user.id
    }
