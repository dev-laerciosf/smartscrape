from dataclasses import dataclass


@dataclass(frozen=True)
class Film:
    title: str
    year: str
    director: str
    average_rating: float
