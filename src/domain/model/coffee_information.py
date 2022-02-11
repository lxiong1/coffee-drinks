"""Coffee information data class"""

from typing import List
from dataclasses import dataclass
from domain.model.coffee_drink import CoffeeDrink


@dataclass
class CoffeeInformation:
    """Model for holding information about all coffee drinks"""

    def __init__(self, coffee_drinks: List[CoffeeDrink]):
        self.coffee_drinks = coffee_drinks

    coffee_drinks: List[CoffeeDrink]
