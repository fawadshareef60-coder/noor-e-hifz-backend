# Routers module initializer pipeline
# Is se mainapp dynamic syntax resolution fetch karega

from .auth import router as auth_router
from .profiles import router as profiles_router
from .quran import router as quran_router
from .lessons import router as lessons_router
from .recordings import router as recordings_router
from .ai_assessments import router as ai_assessments_router
from .analytics import router as analytics_router
from .support import router as support_router
