from typing import Optional

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

import structlog

logger = structlog.get_logger(__name__)

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    SECRET_KEY: SecretStr = Field(default="*")
    JWT_SECRET_KEY: Optional[str] = Field(default="insecure-jwt-secret-key")
    DJANGO_ALLOW_ASYNC_UNSAFE: str = Field(default="true")

    model_config = SettingsConfigDict(
        env_file=".env",
        use_enum_values=True,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="allow",
    )


settings = Settings()
logger.info("Settings", settings=settings)
