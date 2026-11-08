from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

# ==========================================
# 1. QURAN SURAH REFERENCE MODEL
# ==========================================
class QuranSurah(Base):
    __tablename__ = "quran_surahs"

    surah_number = Column(Integer, primary_key=True, index=True)
    name_arabic = Column(String(100), nullable=False)
    name_english = Column(String(100), nullable=False)
    name_urdu = Column(String(100), nullable=False)
    total_ayahs = Column(Integer, nullable=False)

    # Relationship to link all Ayahs belonging to this Surah
    ayahs = relationship("QuranAyah", back_populates="surah", cascade="all, delete-orphan")

# ==========================================
# 2. QURAN AYAH METADATA & TEXT MODEL
# ==========================================
class QuranAyah(Base):
    __tablename__ = "quran_ayahs"

    id = Column(String(36), primary_key=True, server_default=None) # UUID handled as String for flexibility
    surah_number = Column(Integer, ForeignKey("quran_surahs.surah_number", on_delete="CASCADE"), nullable=False)
    ayah_number = Column(Integer, nullable=False)
    para_number = Column(Integer, nullable=False, index=True) # Para / Juz tracking (1 to 30)
    text_uthmani = Column(Text, nullable=False) # Complete Arabic text with zero errors (Verified)
    text_clean = Column(Text, nullable=False)   # Simple Arabic without Tashkeel for AI speech recognition alignment

    # Relationships
    surah = relationship("QuranSurah", back_populates="ayahs")

    # Guard constraint to ensure no duplicate Ayah entries in a Surah
    __table_args__ = (UniqueConstraint('surah_number', 'ayah_number', name='_surah_ayah_uc'),)
