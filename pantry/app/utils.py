import re
from typing import List

from ..core.exceptions import ParseError
from ..core.types import Ingredient, MealName
from .menu import Meal

REGEX = {
    "meal": re.compile(r"Meal.+?(?=\))"),
    "name": re.compile(r"(?<=MealName\.).+?(?=:)"),
    "ingredient": re.compile(r"(?<=Ingredient\.).+?(?=:)"),
}


def _convert_meal_string_to_meal(meal_string: str) -> Meal:

    name_match = re.search(REGEX["name"], string=meal_string)
    if name_match is None:
        raise ParseError(type_=MealName)
    name = MealName(name_match.group())

    ingredients_match = re.findall(REGEX["ingredient"], string=meal_string)
    if not ingredients_match:
        raise ParseError(type_=Ingredient)
    ingredients = [Ingredient(ingredient) for ingredient in ingredients_match]

    meal = Meal(name=name, ingredients=ingredients)

    return meal


def convert_meal_string_to_meal_single(string: str) -> Meal:

    meal_string_match = re.search(REGEX["meal"], string=string)

    if meal_string_match is None:
        raise ParseError(type_=Meal)
    meal_string = meal_string_match.group()

    return _convert_meal_string_to_meal(meal_string=meal_string)


def convert_meal_string_to_meal_multiple(string: str) -> List[Meal]:

    meals_string_matches = re.findall(REGEX["meal"], string=string)

    if meals_string_matches == []:
        raise ParseError(type_=Meal)

    return [
        _convert_meal_string_to_meal(meal_string=meal)
        for meal in meals_string_matches
    ]
