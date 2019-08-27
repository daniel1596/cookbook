from sqlalchemy.orm import joinedload
from typing import List

from database.Models import Recipe, Ingredient, Step
from database.Setup import reset_data, session


def get_all_ingredients() -> List[Ingredient]:
    return Ingredient.query.all()


def get_all_recipes() -> List[Recipe]:
    return Recipe.query.order_by(Recipe.Name).all()


def get_recipe_by_name(name: str) -> Recipe:
    return Recipe.query\
        .options(joinedload(Recipe.Ingredients))\
        .filter(Recipe.Name.like(f"%{name}%"))\
        .first()  # making it not a part of a session seems to work... is that bad?


# def get_recipes_by_name(name: str) -> List[Recipe]:
#     # Leave .all() on the end of this! It needs to be a list so it can be serialized. Will get errors otherwise.
#     return Recipe.query\
#         .filter(Recipe.Name.like(f"%{name}%"))\
#         .all()
