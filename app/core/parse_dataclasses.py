from typing import Optional
from dataclasses import dataclass


@dataclass
class ServerConfig:
    host: str
    port: int


@dataclass
class DatabaseConfig:
    url: str


@dataclass
class AppConfig:
    application: Optional[ServerConfig]
    database: Optional[DatabaseConfig]
