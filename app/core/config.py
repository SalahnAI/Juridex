import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    MODEL_NAME: str = "gemini-1.5-flash"  # moins cher et rapide
    MAX_PDF_SIZE_MB: int = 15

settings = Settings()
