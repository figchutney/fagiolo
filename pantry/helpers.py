import datetime
import json
from dataclasses import dataclass, field
from pathlib import Path
from random import shuffle

TODAY = datetime.date.today()


@dataclass
class Meal:
    name: str
    ingredients: list[str]
    effort: bool
    frequency: int
    last_used_string: str
    last_used: datetime.date = field(init=False)

    def __post_init__(self):
        self.last_used = datetime.datetime.strptime(
            self.last_used_string, "%Y-%m-%d"
        ).date()


@dataclass
class Menu:
    options: list[Meal]
    meal_count: int
    effort_count: int
    selections: list[Meal] = field(default_factory=list)
    date: datetime.date = field(init=False)

    def __post_init__(self):
        self.date = datetime.date.today()
        if self.meal_count < self.effort_count:
            raise ValueError("Meal count must be greater than or equal to effort count")

    def generate_menu(self):

        self._select_based_on_frequency()
        shuffle(self.selections)
        self._select_based_on_effort()
        shuffle(self.options)
        self._top_up_selections()

        return self.selections

    def _select_based_on_frequency(self):

        for meal in self.options:
            if meal.last_used < TODAY - datetime.timedelta(weeks=meal.frequency):
                self.selections.append(meal)

    def _select_based_on_effort(self):

        effort_true_count = self.effort_count
        effort_false_count = self.meal_count - self.effort_count

        effort_true = [meal for meal in self.selections if meal.effort is True]
        effort_false = [meal for meal in self.selections if meal.effort is False]

        self.selections = (
            effort_true[:effort_true_count] + effort_false[:effort_false_count]
        )

    def _top_up_selections(self):

        if len(self.selections) == self.meal_count:
            return

        for meal in self.options:
            if meal not in self.selections:
                self.selections.append(meal)
            if len(self.selections) == self.meal_count:
                return


def load_json(filename: str) -> dict:

    path = Path(__file__).parent / filename
    with open(path) as f:
        data = json.load(f)

    return data


def get_meals() -> list:

    data = load_json("meals.json")
    meals = [meal for meal in data["meals"]]

    return meals
