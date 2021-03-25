from typing import Type, Union

from ..app.menu import Meal
from . import types


class ParseError(Exception):
    def __init__(
        self,
        type_: Union[Type[Meal], Type[types.MealName], Type[types.Ingredient]],
    ) -> None:

        super().__init__(
            f"Failed to match {type_.__name__}-like object from "
            f"string using RegEx"
        )
