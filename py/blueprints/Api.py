from flask import Blueprint
from jsonpickle import encode

from py.database.Queries import get_all_ingredients, get_all_recipes, get_recipe_by_name


API = Blueprint("API", __name__, url_prefix='/api')


"""
The methods for /api/recipes and /api/ingredients are used on the index page, so leave those methods be! Haha.
/api/recipes/<recipe_name> is used on recipe detail pages.
"""


@API.route("recipes")
def list_from_db():
	return encode(get_all_recipes())


@API.route("recipes/<recipe_name>")
def get_recipe(recipe_name: str):
	return encode(get_recipe_by_name(recipe_name))


@API.route("ingredients")
def list_ingredients() -> str:
	return encode(get_all_ingredients())
