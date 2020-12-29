from pantry.helpers import Meal, Menu, get_meals


def main():
    meals = get_meals()
    menu = Menu(
        options=[
            Meal(
                name=meal["name"],
                ingredients=meal["ingredients"],
                effort=meal["effort"],
                frequency=meal["frequency"],
                last_used_string=meal["last_used"],
            )
            for meal in meals
        ],
        meal_count=7,
        effort_count=3,
    )
    selections = menu.generate_menu()
    return print([selection.name for selection in selections])


if __name__ == "__main__":
    main()
