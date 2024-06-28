from dataclasses import dataclass


@dataclass
class Side(frozen=True, order=True):
    type: str
    color: str
