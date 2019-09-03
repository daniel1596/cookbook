from sqlalchemy.orm import joinedload
from typing import List

from py.database.Models import Recipe, Ingredient


def get_all_ingredients() -> List[Ingredient]:
    return Ingredient.query.all()


def get_all_recipes() -> List[Recipe]:
    return Recipe.query.order_by(Recipe.Name).all()


def get_recipe_by_name(name: str) -> Recipe:
    return Recipe.query\
        .options(joinedload(Recipe.Ingredients))\
        .filter(Recipe.Name.like(f"%{name}%"))\
        .first()  # I am guessing the filtering must be case-insensitive by default
