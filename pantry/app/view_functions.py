import random
from typing import List

from .menu import Meal


def generate_meal_choices(
    menu: List[Meal], number_of_meals: int
) -> List[Meal]:

    random.shuffle(menu)

    return [meal for meal in menu][:number_of_meals]


def swap_meal(
    menu: List[Meal], selection: List[Meal], meal_to_swap: Meal
) -> List[Meal]:

    new_meal = meal_to_swap
    while (new_meal == meal_to_swap) or (new_meal in selection):
        new_meal = generate_meal_choices(menu=menu, number_of_meals=1)[0]
    for i, meal in enumerate(selection):
        if meal == meal_to_swap:
            selection.remove(meal_to_swap)
            selection.insert(i, new_meal)
            return selection
    raise ValueError("The meal to swap could not be found in the selection")
