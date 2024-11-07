"""
Configuration Management
-----------------------
Handles loading and managing environment variables and configuration settings
for the IRM application.
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    """Configuration class to manage environment variables and settings."""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Application Configuration
    APP_ENV = os.getenv('APP_ENV', 'development')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    @classmethod
    def validate(cls):
        """
        Validates that all required configuration variables are set.
        
        Raises:
            ValueError: If any required configuration is missing
        """
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY must be set in environment variables") 