"""Configuration settings loaded from environment variables"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings"""
    
    # Telegram Configuration
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    # User Profile (Nguyễn Hùng Mạnh)
    USER_BIRTH_DAY = int(os.getenv("USER_BIRTH_DAY", 14))
    USER_BIRTH_MONTH = int(os.getenv("USER_BIRTH_MONTH", 4))
    USER_BIRTH_YEAR = int(os.getenv("USER_BIRTH_YEAR", 2001))
    USER_ELEMENT = os.getenv("USER_ELEMENT", "Kim")
    USER_BRANCH = os.getenv("USER_BRANCH", "Tỵ")
    
    # Schedule Configuration
    SCHEDULE_HOUR = int(os.getenv("SCHEDULE_HOUR", 20))  # 8 PM
    TIMEZONE = os.getenv("TIMEZONE", "Asia/Ho_Chi_Minh")
    
    # Health Check Server (for Render.com)
    PORT = int(os.getenv("PORT", 8080))
    
    # Calculate life path number (for numerology)
    @classmethod
    def get_life_path_number(cls) -> int:
        """Calculate user's life path number"""
        from core.numerology import calculate_life_path_number
        return calculate_life_path_number(
            cls.USER_BIRTH_DAY,
            cls.USER_BIRTH_MONTH,
            cls.USER_BIRTH_YEAR
        )
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate that all required settings are present
        
        Returns:
            True if valid, raises ValueError if not
        """
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is required in .env file")
        
        if not cls.TELEGRAM_CHAT_ID:
            raise ValueError("TELEGRAM_CHAT_ID is required in .env file")
        
        return True


# Create settings instance
settings = Settings()
