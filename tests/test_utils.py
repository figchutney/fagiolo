import pytest

from fagiolo.app import utils
from fagiolo.app.menu import Meal
from fagiolo.core.exceptions import ParseError
from fagiolo.core.types import Ingredient, MealName

from .data import DUMMY_MEAL_TO_SWAP_STRING, DUMMY_SELECTION_STRING


def test_convert_meal_string_to_meal_single():
    expected = Meal(
        name=MealName.SAUSAGE_AND_MASH,
        ingredients=[
            Ingredient.SAUSAGE,
            Ingredient.POTATO,
            Ingredient.BROCCOLI,
            Ingredient.RED_ONION,
            Ingredient.VEGETABLE_STOCK,
        ],
    )
    actual = utils.convert_meal_string_to_meal_single(
        DUMMY_MEAL_TO_SWAP_STRING
    )

    assert actual == expected


def test_convert_meal_string_to_meal_parse_errors():

    with pytest.raises(ParseError) as e:
        utils.convert_meal_string_to_meal_single("FOO")
    assert str(e.value) == (
        "Failed to match Meal-like object from string using RegEx"
    )

    with pytest.raises(ParseError) as e:
        utils.convert_meal_string_to_meal_multiple("FOO")
    assert str(e.value) == (
        "Failed to match Meal-like object from string using RegEx"
    )

    with pytest.raises(ParseError) as e:
        utils._convert_meal_string_to_meal("Meal(FOO)")
    assert str(e.value) == (
        "Failed to match MealName-like object from string using RegEx"
    )

    with pytest.raises(ParseError) as e:
        utils._convert_meal_string_to_meal(
            "Meal(name=<MealName.OVEN_PIZZA: 'OVEN_PIZZA'>"
        )
    assert str(e.value) == (
        "Failed to match Ingredient-like object from string using RegEx"
    )


def test_convert_meal_string_to_meal_invalid_enum_member():

    with pytest.raises(ValueError) as e:
        utils._convert_meal_string_to_meal(
            "Meal(name=<MealName.BRICKS_ON_TOAST: 'BRICKS_ON_TOAST'>, "
            "ingredients=[<Ingredient.SOIL: 'SOIL'>"
        )
    assert str(e.value) == ("'BRICKS_ON_TOAST' is not a valid MealName")

    with pytest.raises(ValueError) as e:
        utils._convert_meal_string_to_meal(
            "Meal(name=<MealName.OVEN_PIZZA: 'OVEN_PIZZA'>, "
            "ingredients=[<Ingredient.SOIL: 'SOIL'>"
        )
    assert str(e.value) == ("'SOIL' is not a valid Ingredient")


def test_convert_meal_string_to_meal_multiple():
    expected = [
        Meal(
            name=MealName.COUGETTE_PRAWN_ORZO,
            ingredients=[
                Ingredient.COURGETTE,
                Ingredient.ORZO,
                Ingredient.WHITE_ONION,
                Ingredient.VEGETABLE_STOCK,
                Ingredient.GARLIC,
                Ingredient.PRAWNS,
                Ingredient.PAPRIKA,
                Ingredient.LEMON,
                Ingredient.PARSLEY,
            ],
        ),
        Meal(
            name=MealName.CAULIFLOWER_RISOTTO,
            ingredients=[
                Ingredient.WHITE_ONION,
                Ingredient.CAULIFLOWER,
                Ingredient.THYME,
                Ingredient.VEGETABLE_STOCK,
                Ingredient.RISOTTO_RICE,
                Ingredient.PARMESAN,
                Ingredient.PROSCIUTTO,
            ],
        ),
        Meal(
            name=MealName.STUFFED_MUSHROOMS,
            ingredients=[
                Ingredient.MUSHROOM,
                Ingredient.RICOTTA,
                Ingredient.CHILLI,
                Ingredient.OREGANO,
                Ingredient.LEMON,
                Ingredient.SALAD,
            ],
        ),
        Meal(
            name=MealName.AUBERGINE_MASSAMAN_CURRY,
            ingredients=[
                Ingredient.AUBERGINE,
                Ingredient.BASMATI_RICE,
                Ingredient.CORRIANDER,
                Ingredient.COCONUT_MILK,
                Ingredient.SEASAME_SEEDS,
                Ingredient.LIME,
                Ingredient.MASSAMAN_CURRY_PASTE,
                Ingredient.SPINACH,
            ],
        ),
        Meal(name=MealName.OVEN_PIZZA, ingredients=[Ingredient.OVEN_PIZZA]),
        Meal(
            name=MealName.JERK_CHICKEN_BURGER,
            ingredients=[
                Ingredient.RED_CHILLI,
                Ingredient.CHICKEN_BREAST,
                Ingredient.JERK_SEASONING,
                Ingredient.TINNED_PINEAPPLE_RINGS,
                Ingredient.CARROT,
                Ingredient.WHITE_CABBAGE,
                Ingredient.NATURAL_YOGHURT,
                Ingredient.BRIOCHE_BUNS,
            ],
        ),
        Meal(
            name=MealName.CHICKPEA_CHORIZO_STEW,
            ingredients=[
                Ingredient.TINNED_TOMATOES,
                Ingredient.CHORIZO,
                Ingredient.RED_ONION,
                Ingredient.RED_PEPPER,
                Ingredient.GARLIC,
                Ingredient.PAPRIKA,
                Ingredient.CHICKPEAS,
                Ingredient.RICE,
            ],
        ),
    ]
    actual = utils.convert_meal_string_to_meal_multiple(DUMMY_SELECTION_STRING)

    assert actual == expected
