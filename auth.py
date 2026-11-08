import os
from datetime import datetime, timedelta, timezone
from typing import Optional, Any
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import settings

# 1. Password Hashing Configuration
# passlib automatic bcrypt algorithm use karega secure encryption ke liye
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. JWT Configuration
# In settings ko testing ke baad dev.env file mein daal sakte hain
SECRET_KEY = os.getenv("JWT_SECRET", "NOOR_E_HIFZ_SUPER_SECRET_KEY_987654321_MADRASA")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440 # Token 24 hours tak valid rahega

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_STR}/auth/login")

# ==========================================
# SECURITY UTILITY FUNCTIONS
# ==========================================

def get_password_hash(password: str) -> str:
    """Plain password ko unreadable hashed string mein convert karta hai"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Login ke waqt plain password ko database wale hashed password se match karta hai"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """User login hone par ek secure session JWT token generate karta hai"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ==========================================
# CURRENT USER DEPENDENCY
# ==========================================

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Har us API route par check lagata hai jahan student ka login hona lazmi ho"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials or token expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user_id: str = payload.get("id")
        user_role: str = payload.get("role")
        
        if email is None or user_id is None:
            raise credentials_exception
            
        return {"id": user_id, "email": email, "role": user_role}
        
    except JWTError:
        raise credentials_exception
