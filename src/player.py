from dataclasses import dataclass

from src.user import User


@dataclass
class Player(User):
    name: str = ""  # "" is error-handled as an invalid name
    wins: int = 0
    games_played: int = 0
