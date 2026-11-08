from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models_quran import QuranSurah

# Comprehensive verified reference checklist for initial 30 Surahs setup 
# Mobile apps aur analytics engine is list ke indexes se math calculate karte hain
QURAN_SURAH_DATA = [
    {"surah_number": 1, "name_arabic": "الفاتحة", "name_english": "Al-Fatiha", "name_urdu": "الفاتحة", "total_ayahs": 7},
    {"surah_number": 2, "name_arabic": "البقرة", "name_english": "Al-Baqarah", "name_urdu": "البقرة", "total_ayahs": 286},
    {"surah_number": 3, "name_arabic": "آل عمران", "name_english": "Ali 'Imran", "name_urdu": "آل عمران", "total_ayahs": 200},
    {"surah_number": 4, "name_arabic": "النساء", "name_english": "An-Nisa", "name_urdu": "النساء", "total_ayahs": 176},
    {"surah_number": 5, "name_arabic": "المائدة", "name_english": "Al-Ma'idah", "name_urdu": "المائدة", "total_ayahs": 120},
    {"surah_number": 6, "name_arabic": "الأنعام", "name_english": "Al-An'am", "name_urdu": "الأنعام", "total_ayahs": 165},
    {"surah_number": 7, "name_arabic": "الأعراف", "name_english": "Al-A'raf", "name_urdu": "الأعراف", "total_ayahs": 206},
    {"surah_number": 8, "name_arabic": "الأنفال", "name_english": "Al-Anfal", "name_urdu": "الأنفال", "total_ayahs": 75},
    {"surah_number": 9, "name_arabic": "التوبة", "name_english": "At-Tawbah", "name_urdu": "التوبة", "total_ayahs": 129},
    {"surah_number": 10, "name_arabic": "يونس", "name_english": "Yunus", "name_urdu": "يونس", "total_ayahs": 109},
    {"surah_number": 11, "name_arabic": "هود", "name_english": "Hud", "name_urdu": "هود", "total_ayahs": 123},
    {"surah_number": 12, "name_arabic": "يوسف", "name_english": "Yusuf", "name_urdu": "يوسف", "total_ayahs": 111},
    {"surah_number": 13, "name_arabic": "الرعد", "name_english": "Ar-Ra'd", "name_urdu": "الرعد", "total_ayahs": 43},
    {"surah_number": 14, "name_arabic": "ابراهيم", "name_english": "Ibrahim", "name_urdu": "ابراهيم", "total_ayahs": 52},
    {"surah_number": 15, "name_arabic": "الحجر", "name_english": "Al-Hijr", "name_urdu": "الحجر", "total_ayahs": 99},
    {"surah_number": 16, "name_arabic": "النحل", "name_english": "An-Nahl", "name_urdu": "النحل", "total_ayahs": 128},
    {"surah_number": 17, "name_arabic": "الإسراء", "name_english": "Al-Isra", "name_urdu": "بنی اسرائیل", "total_ayahs": 111},
    {"surah_number": 18, "name_arabic": "الكهف", "name_english": "Al-Kahf", "name_urdu": "الكهف", "total_ayahs": 110},
    {"surah_number": 19, "name_arabic": "مريم", "name_english": "Maryam", "name_urdu": "مريم", "total_ayahs": 98},
    {"surah_number": 20, "name_arabic": "طه", "name_english": "Ta-Ha", "name_urdu": "طہ", "total_ayahs": 135},
    {"surah_number": 21, "name_arabic": "الأنبياء", "name_english": "Al-Anbiya", "name_urdu": "الأنبیاء", "total_ayahs": 112},
    {"surah_number": 22, "name_arabic": "الحج", "name_english": "Al-Hajj", "name_urdu": "الحج", "total_ayahs": 78},
    {"surah_number": 23, "name_arabic": "المؤمنون", "name_english": "Al-Mu'minun", "name_urdu": "المؤمنون", "total_ayahs": 118},
    {"surah_number": 24, "name_arabic": "النور", "name_english": "An-Nur", "name_urdu": "النور", "total_ayahs": 64},
    {"surah_number": 25, "name_arabic": "الفرقان", "name_english": "Al-Furqan", "name_urdu": "الفرقان", "total_ayahs": 77},
    {"surah_number": 26, "name_arabic": "الشعراء", "name_english": "Ash-Shu'ara", "name_urdu": "الشعراء", "total_ayahs": 227},
    {"surah_number": 27, "name_arabic": "النمل", "name_english": "An-Naml", "name_urdu": "النمل", "total_ayahs": 93},
    {"surah_number": 28, "name_arabic": "القصص", "name_english": "Al-Qasas", "name_urdu": "القصص", "total_ayahs": 88},
    {"surah_number": 29, "name_arabic": "العنكبوت", "name_english": "Al-'Ankabut", "name_urdu": "العنکبوت", "total_ayahs": 69},
    {"surah_number": 30, "name_arabic": "الروم", "name_english": "Ar-Rum", "name_urdu": "الروم", "total_ayahs": 60}
]

def seed_master_surahs():
    """
    Database session initiate karke check karta hai ke agar tables empty hain 
    toh Quran metadata pipelines feed kar sake.
    """
    db: Session = SessionLocal()
    try:
        print("Quran metadata validation check shuru ho rahi hai...")
        for surah in QURAN_SURAH_DATA:
            # Check if record already seeded
            exists = db.query(QuranSurah).filter(QuranSurah.surah_number == surah["surah_number"]).first()
            if not exists:
                new_surah = QuranSurah(
                    surah_number=surah["surah_number"],
                    name_arabic=surah["name_arabic"],
                    name_english=surah["name_english"],
                    name_urdu=surah["name_urdu"],
                    total_ayahs=surah["total_ayahs"]
                )
                db.add(new_surah)
                print(f"Surah {surah['name_english']} successfully maps update ho gayi.")
        
        db.commit()
        print("Alhamdulillah, Master Quran reference configuration data seeded successfully.")
    except Exception as e:
        db.rollback()
        print(f"Seeding process error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_master_surahs()
