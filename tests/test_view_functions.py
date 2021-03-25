import copy

import pytest

from pantry.app import view_functions
from pantry.app.menu import MENU

from .data import (
    DUMMY_MEAL_TO_SWAP,
    DUMMY_MEAL_TO_SWAP_NOT_IN_SELECTION,
    DUMMY_SELECTION,
)


def test_generate_meal_choices():
    """It would be nice to find a good way of testing randomness here"""

    actual = view_functions.generate_meal_choices(menu=MENU, number_of_meals=7)

    assert len(actual) == 7


def test_swap_meal():
    """It would be nice to find a good way of testing randomness here"""

    old_selection = copy.copy(DUMMY_SELECTION)
    new_selection = view_functions.swap_meal(
        menu=MENU,
        selection=DUMMY_SELECTION,
        meal_to_swap=DUMMY_MEAL_TO_SWAP,
    )

    assert len(new_selection) == len(DUMMY_SELECTION)

    # Check order has been preserved
    assert new_selection[0] == old_selection[0]
    assert new_selection[1] == old_selection[1]
    assert new_selection[2] != old_selection[2]  # The swapped meal
    assert new_selection[3] == old_selection[3]
    assert new_selection[4] == old_selection[4]
    assert new_selection[5] == old_selection[5]
    assert new_selection[6] == old_selection[6]


def test_swap_meal_error():

    with pytest.raises(ValueError) as e:
        view_functions.swap_meal(
            menu=MENU,
            selection=DUMMY_SELECTION,
            meal_to_swap=DUMMY_MEAL_TO_SWAP_NOT_IN_SELECTION,
        )
    assert str(e.value) == (
        "The meal to swap could not be found in the selection"
    )
