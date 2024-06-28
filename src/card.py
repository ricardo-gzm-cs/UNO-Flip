from dataclasses import dataclass

from src.side import Side


@dataclass(frozen=True, order=True)
class Card:
    light_side: Side
    dark_side: Side
