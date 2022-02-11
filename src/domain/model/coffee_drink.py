"""Coffee drink data class"""

from dataclasses import dataclass
from typing import List


@dataclass
class CoffeeDrink:
    """Model for holding information about a specific coffee drink"""

    id: str  # pylint: disable=C0103
    title: str
    description: str
    ingredients: List[str]
