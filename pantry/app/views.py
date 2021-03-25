from typing import Any

from flask import render_template, request

from ..app import app
from .menu import MENU
from .utils import (
    convert_meal_string_to_meal_multiple,
    convert_meal_string_to_meal_single,
)
from .view_functions import generate_meal_choices, swap_meal

DEAFULT_MEAL_COUNT = str(7)


@app.route("/", methods=["POST", "GET"])
def root() -> Any:

    if request.form.get("meal-to-swap") is not None:

        selection = convert_meal_string_to_meal_multiple(
            request.form.get("selection", "")
        )
        meal_to_swap = convert_meal_string_to_meal_single(
            request.form.get("meal-to-swap", "")
        )
        number_of_meals = request.form.get("number-of-meals")
        updated_selection = swap_meal(
            menu=MENU,
            selection=selection,
            meal_to_swap=meal_to_swap,
        )
        return render_template(
            "root.html",
            selection=updated_selection,
            number_of_meals=number_of_meals,
        )

    number_of_meals = int(request.form.get("meals", DEAFULT_MEAL_COUNT))
    selection = generate_meal_choices(
        menu=MENU,
        number_of_meals=number_of_meals,
    )

    return render_template(
        "root.html",
        selection=selection,
        number_of_meals=str(number_of_meals),
    )
