from fagiolo.app.menu import Meal
from fagiolo.core.types import Ingredient, MealName

DUMMY_SELECTION_STRING = "[Meal(name=<MealName.COUGETTE_PRAWN_ORZO: 'COUGETTE_PRAWN_ORZO'>, ingredients=[<Ingredient.COURGETTE: 'COURGETTE'>, <Ingredient.ORZO: 'ORZO'>, <Ingredient.WHITE_ONION: 'WHITE_ONION'>, <Ingredient.VEGETABLE_STOCK: 'VEGETABLE_STOCK'>, <Ingredient.GARLIC: 'GARLIC'>, <Ingredient.PRAWNS: 'PRAWNS'>, <Ingredient.PAPRIKA: 'PAPRIKA'>, <Ingredient.LEMON: 'LEMON'>, <Ingredient.PARSLEY: 'PARSLEY'>]), Meal(name=<MealName.CAULIFLOWER_RISOTTO: 'CAULIFLOWER_RISOTTO'>, ingredients=[<Ingredient.WHITE_ONION: 'WHITE_ONION'>, <Ingredient.CAULIFLOWER: 'CAULIFLOWER'>, <Ingredient.THYME: 'THYME'>, <Ingredient.VEGETABLE_STOCK: 'VEGETABLE_STOCK'>, <Ingredient.RISOTTO_RICE: 'RISOTTO_RICE'>, <Ingredient.PARMESAN: 'PARMESAN'>, <Ingredient.PROSCIUTTO: 'PROSCIUTTO'>]), Meal(name=<MealName.STUFFED_MUSHROOMS: 'STUFFED_MUSHROOMS'>, ingredients=[<Ingredient.MUSHROOM: 'MUSHROOM'>, <Ingredient.RICOTTA: 'RICOTTA'>, <Ingredient.CHILLI: 'CHILLI'>, <Ingredient.OREGANO: 'OREGANO'>, <Ingredient.LEMON: 'LEMON'>, <Ingredient.SALAD: 'SALAD'>]), Meal(name=<MealName.AUBERGINE_MASSAMAN_CURRY: 'AUBERGINE_MASSAMAN_CURRY'>, ingredients=[<Ingredient.AUBERGINE: 'AUBERGINE'>, <Ingredient.BASMATI_RICE: 'BASMATI_RICE'>, <Ingredient.CORRIANDER: 'CORRIANDER'>, <Ingredient.COCONUT_MILK: 'COCONUT_MILK'>, <Ingredient.SEASAME_SEEDS: 'SEASAME_SEEDS'>, <Ingredient.LIME: 'LIME'>, <Ingredient.MASSAMAN_CURRY_PASTE: 'MASSAMAN_CURRY_PASTE'>, <Ingredient.SPINACH: 'SPINACH'>]), Meal(name=<MealName.OVEN_PIZZA: 'OVEN_PIZZA'>, ingredients=[<Ingredient.OVEN_PIZZA: 'OVEN_PIZZA'>]), Meal(name=<MealName.JERK_CHICKEN_BURGER: 'JERK_CHICKEN_BURGER'>, ingredients=[<Ingredient.RED_CHILLI: 'RED_CHILLI'>, <Ingredient.CHICKEN_BREAST: 'CHICKEN_BREAST'>, <Ingredient.JERK_SEASONING: 'JERK_SEASONING'>, <Ingredient.TINNED_PINEAPPLE_RINGS: 'TINNED_PINEAPPLE_RINGS'>, <Ingredient.CARROT: 'CARROT'>, <Ingredient.WHITE_CABBAGE: 'WHITE_CABBAGE'>, <Ingredient.NATURAL_YOGHURT: 'NATURAL_YOGHURT'>, <Ingredient.BRIOCHE_BUNS: 'BRIOCHE_BUNS'>]), Meal(name=<MealName.CHICKPEA_CHORIZO_STEW: 'CHICKPEA_CHORIZO_STEW'>, ingredients=[<Ingredient.TINNED_TOMATOES: 'TINNED_TOMATOES'>, <Ingredient.CHORIZO: 'CHORIZO'>, <Ingredient.RED_ONION: 'RED_ONION'>, <Ingredient.RED_PEPPER: 'RED_PEPPER'>, <Ingredient.GARLIC: 'GARLIC'>, <Ingredient.PAPRIKA: 'PAPRIKA'>, <Ingredient.CHICKPEAS: 'CHICKPEAS'>, <Ingredient.RICE: 'RICE'>])]"  # noqa
DUMMY_MEAL_TO_SWAP_STRING = "Meal(name=<MealName.SAUSAGE_AND_MASH: 'SAUSAGE_AND_MASH'>, ingredients=[<Ingredient.SAUSAGE: 'SAUSAGE'>, <Ingredient.POTATO: 'POTATO'>, <Ingredient.BROCCOLI: 'BROCCOLI'>, <Ingredient.RED_ONION: 'RED_ONION'>, <Ingredient.VEGETABLE_STOCK: 'VEGETABLE_STOCK'>])"  # noqa

DUMMY_SELECTION = [
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
DUMMY_MEAL_TO_SWAP = Meal(
    name=MealName.STUFFED_MUSHROOMS,
    ingredients=[
        Ingredient.MUSHROOM,
        Ingredient.RICOTTA,
        Ingredient.CHILLI,
        Ingredient.OREGANO,
        Ingredient.LEMON,
        Ingredient.SALAD,
    ],
)
DUMMY_MEAL_TO_SWAP_NOT_IN_SELECTION = Meal(
    name=MealName.SAUSAGE_AND_MASH,
    ingredients=[
        Ingredient.SAUSAGE,
        Ingredient.POTATO,
        Ingredient.BROCCOLI,
        Ingredient.RED_ONION,
        Ingredient.VEGETABLE_STOCK,
    ],
)
