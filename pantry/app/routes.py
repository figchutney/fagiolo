from flask import render_template, request

from pantry.app import app
from pantry.app_services.generate import generate_meal_choices, generate_menu


@app.route("/", methods=["POST", "GET"])
def root():

    menu = generate_menu()

    number_of_meals = int(request.form.get("meals", "7"))
    selections = generate_meal_choices(
        menu=menu,
        number_of_meals=number_of_meals,
    )
    return render_template(
        "root.html",
        selections=selections,
        number_of_meals=str(number_of_meals),
    )
