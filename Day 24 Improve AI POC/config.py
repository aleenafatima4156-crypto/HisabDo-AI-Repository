import os

class Config:
    APP_NAME = "HisabDo AI Help & Support"
    API_VERSION = "1.0"
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", "5000"))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
