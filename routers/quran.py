from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models_quran import QuranSurah, QuranAyah

router = APIRouter(
    prefix="/quran",
    tags=["Quranic Text & Content Engine"]
)

# ==========================================
# 1. FETCH ALL SURAHS (SURAH LIST)
# ==========================================
@router.get("/surahs", response_model=List[dict])
def get_all_surahs(db: Session = Depends(get_db)):
    """
    Quran Pak ki tamaam 114 Surahs ki list unke Arabic, English aur Urdu naam ke sath fetch karta hai.
    """
    surahs = db.query(QuranSurah).order_by(QuranSurah.surah_number).all()
    return [
        {
            "surah_number": s.surah_number,
            "name_arabic": s.name_arabic,
            "name_english": s.name_english,
            "name_urdu": s.name_urdu,
            "total_ayahs": s.total_ayahs
        }
        for s in surahs
    ]

# ==========================================
# 2. FETCH SPECIFIC PARA / JUZ (1 to 30)
# ==========================================
@router.get("/para/{para_number}", response_model=List[dict])
def get_ayahs_by_para(para_number: int, db: Session = Depends(get_db)):
    """
    Para number (1 se 30) ke mutabiq us Para ki tamaam Ayahs aur unka verified text complete sequence mein laata hai.
    """
    if para_number < 1 or para_number > 30:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ghalat Para number! Para number 1 se 30 ke darmiyan hona chahiye."
        )
        
    ayahs = db.query(QuranAyah).filter(QuranAyah.para_number == para_number).order_by(QuranAyah.surah_number, QuranAyah.ayah_number).all()
    return [
        {
            "id": str(a.id),
            "surah_number": a.surah_number,
            "ayah_number": a.ayah_number,
            "text_uthmani": a.text_uthmani,
            "text_clean": a.text_clean
        }
        for a in ayahs
    ]

# ==========================================
# 3. FETCH TEXT BY SURAH NUMBER
# ==========================================
@router.get("/surah/{surah_number}", response_model=List[dict])
def get_ayahs_by_surah(surah_number: int, db: Session = Depends(get_db)):
    """
    Specific Surah number ke mutabiq us Surah ki saari Ayahs ka authentic Uthmani script return karta hai.
    """
    if surah_number < 1 or surah_number > 114:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ghalat Surah number! Surah number 1 se 114 ke darmiyan hona chahiye."
        )
        
    ayahs = db.query(QuranAyah).filter(QuranAyah.surah_number == surah_number).order_by(QuranAyah.ayah_number).all()
    return [
        {
            "id": str(a.id),
            "ayah_number": a.ayah_number,
            "para_number": a.para_number,
            "text_uthmani": a.text_uthmani
        }
        for a in ayahs
    ]
