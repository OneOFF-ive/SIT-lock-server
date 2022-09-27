from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    db: str


@dataclass
class LockConfig:
    card_id: str
    mac_id: str
    base_url: str


@dataclass
class Config:
    database: DatabaseConfig
    lock: LockConfig


__all__ = [
    "DatabaseConfig",
    "LockConfig",
    "Config",
]
