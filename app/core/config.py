import os
from pydantic import BaseSettings
from dotenv import load_dotenv

# Carregar o arquivo .env (use o .env padrão localmente)
load_dotenv()

class Settings(BaseSettings):
    CORS_ORIGINS: list[str] = os.getenv("CORS_ORIGINS", "").split(",")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    API_VERSION: str = os.getenv("API_VERSION", "/api/v1")

    class Config:
        env_file = ".env"

settings = Settings()
