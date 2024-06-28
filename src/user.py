from dataclasses import dataclass, field

from src.card import Card


@dataclass
class User(frozen=True, order=True):
    hand: list[Card] = field(default_factory=list, compare=False)
