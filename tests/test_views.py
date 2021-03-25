from bs4 import BeautifulSoup
from flask.testing import FlaskClient

from pantry.testing import (
    ingredient_string_to_enum_multiple,
    meal_name_string_to_enum,
)


def test_root_static(client: FlaskClient):

    resp = client.get("/")
    assert resp.status_code == 200

    page_el = BeautifulSoup(resp.data)

    # FORM - MAIN
    form_main = page_el.find_all("form")[0]
    assert form_main["method"] == "POST"
    assert form_main["action"] == "/"
    assert form_main["id"] == "form-main"

    form_main_input = form_main.find_all("input")[0]
    assert form_main_input["type"] == "number"
    assert form_main_input["min"] == "1"
    assert form_main_input["max"] == "14"
    assert form_main_input["step"] == "1"
    assert form_main_input["id"] == "meals"
    assert form_main_input["name"] == "meals"
    assert form_main_input["value"] == "7"  # 7 is the default
    assert form_main_input["required"] == ""

    form_main_button_minus = form_main.find_all("button")[0]
    assert form_main_button_minus["type"] == "button"
    assert form_main_button_minus["onclick"] == (
        "this.parentNode.querySelector('[type=number]').stepDown();"
        "document.getElementById('form-main').submit();"
    )
    assert (
        form_main_button_minus.text.replace(r"\n", "").strip() == "-"
    )  # Would be nice to not need to replace and strip

    form_main_button_plus = form_main.find_all("button")[1]
    assert form_main_button_plus["type"] == "button"
    assert form_main_button_plus["onclick"] == (
        "this.parentNode.querySelector('[type=number]').stepUp();"
        "document.getElementById('form-main').submit();"
    )
    assert (
        form_main_button_plus.text.replace(r"\n", "").strip() == "+"
    )  # Would be nice to not need to replace and strip

    # FORM - SWAP

    form_swap = page_el.find_all("form")[1]
    assert form_swap["method"] == "POST"
    assert form_swap["action"] == "/"
    assert form_swap["id"] == "form-swap"

    form_swap_input_selection = form_swap.find_all("input")[0]
    assert form_swap_input_selection["type"] == "hidden"
    assert form_swap_input_selection["id"] == "selection"
    assert form_swap_input_selection["name"] == "selection"
    assert form_swap_input_selection["readonly"] == ""
    form_swap_input_meal_to_swap = form_swap.find_all("input")[1]
    assert form_swap_input_meal_to_swap["type"] == "hidden"
    assert form_swap_input_meal_to_swap["id"] == "meal-to-swap"
    assert form_swap_input_meal_to_swap["name"] == "meal-to-swap"
    assert form_swap_input_meal_to_swap["readonly"] == ""
    form_swap_input_number_of_meals = form_swap.find_all("input")[2]
    assert form_swap_input_number_of_meals["type"] == "hidden"
    assert form_swap_input_number_of_meals["id"] == "number-of-meals"
    assert form_swap_input_number_of_meals["name"] == "number-of-meals"
    assert form_swap_input_number_of_meals["readonly"] == ""

    form_swap_button = form_swap.find_all("button")[0]
    assert form_swap_button["type"] == "submit"
    assert form_swap_button.text == "⟳"

    # TABLE

    table = page_el.find_all("table")[0]
    table_rows = table.find_all("tr")

    assert len(table_rows) == 7  # 7 is the default number of meals

    for row in table_rows:
        table_column_meal_name = row("td")[0]
        table_column_ingredients = row("td")[1]
        table_column_swap = row("td")[2]

        assert table_column_meal_name["class"] == ["meal-name"]
        table_column_meal_name_text = table_column_meal_name.text.replace(
            r"\n", ""
        ).strip()  # Would be nice to not need to replace and strip
        meal_name_string_to_enum(
            table_column_meal_name_text
        )  # Will raise exception if text not string repr of MealName member

        assert table_column_ingredients["class"] == ["ingredients"]
        table_column_ingredients_text = table_column_ingredients.text.replace(
            r"\n", ""
        ).strip()  # Would be nice to not need to replace and strip
        ingredient_string_to_enum_multiple(
            table_column_ingredients_text
        )  # Will raise exception if text not string repr of Ingredient member

        assert table_column_swap["class"] == ["swap"]
        assert table_column_swap.find_parent("form")["id"] == "form-swap"


def test_root_non_default_number_of_meals(client: FlaskClient):

    resp = client.post(
        "/",
        data={
            "meals": "3",
        },
    )
    assert resp.status_code == 200

    page_el = BeautifulSoup(resp.data)
    table = page_el.find_all("table")[0]
    table_rows = table.find_all("tr")
    assert len(table_rows) == 3


def test_root_swap(client: FlaskClient):

    # PRE-SWAP

    resp = client.post(
        "/",
        data={
            "meals": "3",
        },
    )

    page_el = BeautifulSoup(resp.data)
    table = page_el.find_all("table")[0]
    table_rows = table.find_all("tr")

    row_one = table_rows[0]
    row_two = table_rows[1]
    row_three = table_rows[2]

    table_column_meal_name_one = row_one("td")[0].text
    table_column_meal_name_two = row_two("td")[0].text
    table_column_meal_name_three = row_three("td")[0].text
    table_column_ingredients_one = row_one("td")[1].text
    table_column_ingredients_two = row_two("td")[1].text
    table_column_ingredients_three = row_three("td")[1].text

    table_column_swap_one = row_one("td")[2]
    table_column_swap_one_selection = table_column_swap_one("input")[0][
        "value"
    ]
    table_column_swap_one_meal_to_swap = table_column_swap_one("input")[1][
        "value"
    ]
    table_column_swap_one_number_of_meals = table_column_swap_one("input")[2][
        "value"
    ]

    # POST-SWAP

    resp_swap = client.post(
        "/",
        data={
            "selection": table_column_swap_one_selection,
            "meal-to-swap": table_column_swap_one_meal_to_swap,
            "number-of-meals": table_column_swap_one_number_of_meals,
        },
    )

    swap_page_el = BeautifulSoup(resp_swap.data)
    swap_table = swap_page_el.find_all("table")[0]
    swap_table_rows = swap_table.find_all("tr")

    swap_row_one = swap_table_rows[0]
    swap_row_two = swap_table_rows[1]
    swap_row_three = swap_table_rows[2]

    swap_table_column_meal_name_one = swap_row_one("td")[0].text
    swap_table_column_meal_name_two = swap_row_two("td")[0].text
    swap_table_column_meal_name_three = swap_row_three("td")[0].text
    swap_table_column_ingredients_one = swap_row_one("td")[1].text
    swap_table_column_ingredients_two = swap_row_two("td")[1].text
    swap_table_column_ingredients_three = swap_row_three("td")[1].text

    # CHECKS (make sure all are the same, except the one we swapped)

    assert table_column_meal_name_one != swap_table_column_meal_name_one
    assert table_column_meal_name_two == swap_table_column_meal_name_two
    assert table_column_meal_name_three == swap_table_column_meal_name_three
    assert table_column_ingredients_one != swap_table_column_ingredients_one
    assert table_column_ingredients_two == swap_table_column_ingredients_two
    assert (
        table_column_ingredients_three == swap_table_column_ingredients_three
    )
