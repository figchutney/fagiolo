from dataclasses import dataclass
from typing import List
from random import shuffle
from pathlib import Path
import json

MEAL_DATA = "meal_bank.json"


@dataclass
class Meal:
    name: str
    ingredients: List[str]


def generate_menu() -> List[Meal]:

    meal_bank = load_json(filename=MEAL_DATA)

    menu = [
        Meal(
            name=meal,
            ingredients=meal_bank[meal]["ingredients"],
        )
        for meal in meal_bank
    ]

    return menu


def generate_meal_choices(menu: List[Meal], number_of_meals: int):

    shuffle(menu)

    return [meal for meal in menu][:number_of_meals]


def swap_meal(
    menu: List[Meal], current_selections: List[Meal], meal_to_swap: Meal
) -> Meal:

    new_meal = "".join(generate_meal_choices(menu=menu, number_of_meals=1))
    for meal in current_selections:
        if meal == meal_to_swap:
            current_selections.remove(meal_to_swap)
            return current_selections.insert(meal, new_meal)


def load_json(filename: str) -> dict:

    path = Path(__file__).parent / filename
    with open(path) as f:
        data = json.load(f)

    return data
