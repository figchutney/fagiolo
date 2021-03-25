from typing import List

from .core.types import Ingredient, MealName


def meal_name_string_to_enum(string: str) -> MealName:
    """Converts a meal name in string-y form like 'Oven Pizza' to the
    corresponding enum member"""

    return MealName(string.replace(" ", "_").upper())


def _ingredient_string_to_enum_single(string: str) -> Ingredient:
    """Converts an ingredient in string-y form like 'smoked paprika' to the
    corresponding enum member"""

    return Ingredient(string.replace(" ", "_").upper())


def ingredient_string_to_enum_multiple(string: str) -> List[Ingredient]:
    """Converts a list of ingredients in string-y form like
    'smoked paprika, mince meat, pasta' to a list of corresponding enum
    members"""

    list_of_strings = string.split(", ")

    return [
        _ingredient_string_to_enum_single(string.replace(" ", "_").upper())
        for string in list_of_strings
    ]
