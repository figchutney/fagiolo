# `fagiolo` 🥘

A weekly meal choice automator 🤖🥘

👉 Have a play around at https://fagiolo.herokuapp.com/

- [`fagiolo` 🥘](#fagiolo-)
  - [Description](#description)
  - [Development](#development)
    - [Setup](#setup)
    - [Running the App](#running-the-app)
    - [Formatting / Style](#formatting--style)
    - [Linting](#linting)
    - [Typing](#typing)
    - [Tests](#tests)
    - [CI/CD](#cicd)
    - [Deployment](#deployment)
  - [Adding a New Meal](#adding-a-new-meal)

## Description

Instead of having to try and remember which meals you like while planning your weekly menu, `fagiolo` allows you to randomly generate as many as you like (well, up to 14) from an ever-expanding bank of tasty meals (including the famous Oven Pizza). If you don't like any of them, you can swap them out for another.

The point isn't to show you *how* to cook things (it's assumed you know this already / can find out), it's just to give a bit of inspiration when you can't decide what to have.

## Development

### Setup

- clone the repo
- make sure you're using Python 3.8 ([asdf](https://asdf-vm.com/#/) is good for managing multiple versions)
- create a virtual environment and install requirements from `requirements-dev.txt` - with the project as my current working directory, I tend to always just do:

```zsh
rm -rf .env; python -m venv .env; source .env/bin/activate; python -m pip install -U pip; python -m pip install -r requirements-dev.txt;
```

### Running the App

- run the app with `flask run`
- navigate to `localhost:5000` in your browser

### Formatting / Style

[`black`](https://github.com/psf/black) is used for formatting, with a max line length of 79. [`isort`](https://pycqa.github.io/isort/) is used for sorting imports.

- format code with `bin/format`

### Linting

[`flake8`](https://flake8.pycqa.org/en/latest/) is used for linting, with a line length of 79.

- run linting checks with `bin/check`

### Typing

[`mypy`](http://mypy-lang.org/) is used to enforce the use of [typehints](https://www.python.org/dev/peps/pep-0484/) and check for type safety.

- run type checks with `bin/check`

### Tests

[`pytest`](https://docs.pytest.org/en/stable/index.html) is used for testing. Minimum test coverage is 100%. Tests live in `tests/` and will only be run by `pytest` if the module and function name is prefixed with `test_`. 

- run tests with `pytest tests`

### CI/CD

Whenever you push a new commit, the `CI` GitHub action (defined in `.github/workflows/main.yml`) will run, which:

- uses Python 3.8
- installs dependences from `requirements-dev.txt`
- checks imports with `isort`
- checks formatting with `black`
- lints code with `flake8`
- checks code scurity with `bandit`
- checks dependency security with `safety`
- checks type safety with `mpypy`
- runs tests in `tests/` with `pytest`

Pull requests can only be merged if the CI checks all pass.

The repo is hooked up with Heroku, so when a merge is made to `main` branch, it triggers a build and deployment in Heroku (more below).

### Deployment

`fagiolo` is deployed using Heroku on a free Dyno.

Heroku is hooked up with the GitHub repo so that merges to `main` trigger a build in Heroku, which results in a deployment if successful.

The deployment is configured with two files in the root directory of the project:

- `Procfile` (runs the app with `gunicorn`)
- `runtime.txt` (tells Heroku to use Python 3.8)

## Adding a New Meal

- check the meal doesn't exist in `MealName` already in `fagiolo/core/types.py`
- add a new member to the `MealName` enum, retaining alphabetical order
- check if you need to add any new ingredients by having a look in `Ingredient` in `fagiolo/core/types.py`
- add any required new ingredients to the `Ingredient` enum, retaining alphabetical order (try and keep things singular unless it looks dumb - e.g. go with `POTATO` instead of `POTATOES`, but `WALNUTS` instead of `WALNUT`)
- add a new instance of `Meal` to the `MEALS` list in `fagiolo/app/menu.py`, where:
   - `name` is a member of `MealName`
   - `ingredients` is a list of members of `Ingredient` 
