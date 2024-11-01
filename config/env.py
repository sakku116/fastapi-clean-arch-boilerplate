import os
from dataclasses import dataclass

from utils.helper import parseBool


@dataclass(frozen=True)
class Env:
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    PRODUCTION: bool = parseBool(os.getenv("PRODUCTION", "false"))
    DEBUG: bool = parseBool(os.getenv("DEBUG", "true"))
    RELOAD: bool = parseBool(os.getenv("RELOAD", "false"))
    TZ: str = os.getenv("TZ", "Asia/Jakarta")
    WORKERS: int = int(os.getenv("WORKERS", 1))