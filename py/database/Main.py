from sqlalchemy.orm import joinedload
from typing import List

from py.database.Models import Recipe, Ingredient


def get_all_ingredients() -> List[Ingredient]:
    return Ingredient.query.all()


def get_all_recipes() -> List[Recipe]:
    return Recipe.query.order_by(Recipe.Name).all()


def get_recipe_by_name(name: str) -> Recipe:
    recipe = Recipe.query\
        .options(joinedload(Recipe.Ingredients))\
        .filter(Recipe.Name.like(f"%{name}%"))\
        .first()  # I am guessing the filtering must be case-insensitive by default

    # For unknown reasons, SQLAlchemy is auto-sorting the list by ingredient name, it seems like
    #  so I have to do this to get around that
    recipe.Ingredients.sort(key=lambda ingredient: ingredient.IngredientID)

    return recipe
