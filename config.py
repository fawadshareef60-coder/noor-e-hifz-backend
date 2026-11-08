from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Noor-e-Hifz AI Digital Madrasa"
    VERSION: str = "1.0"
    API_STR: str = "/api/v1"
    DATABASE_URL: str

    # Chromebook ke liye dev.env file map ki hai
    model_config = SettingsConfigDict(env_file="dev.env", extra="ignore")

settings = Settings()
