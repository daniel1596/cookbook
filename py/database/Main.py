from sqlalchemy.orm import joinedload
from typing import List

from py.database.Models import Recipe, Ingredient


def get_all_ingredients() -> List[Ingredient]:
    return Ingredient.query.all()


def get_all_recipes() -> List[Recipe]:
    return Recipe.query.order_by(Recipe.Name).all()


def get_recipe_by_name(name: str) -> Recipe:
    # TODO major bug. The joinedload causes sqlalchemy to sort the ingredients in order,
    #  but I don't want that. And I have to joinedload or else the ingredients won't show up. Tricky!
    #  Unless I make a separate query for the ingredients, but that seems silly.

    x = Recipe.query\
        .options(joinedload(Recipe.Ingredients))\
        .filter(Recipe.Name.like(f"%{name}%"))\
        .first()  # I am guessing the filtering must be case-insensitive by default

    return x
