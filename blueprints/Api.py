from flask import Blueprint, render_template
from jsonpickle import encode

from database.Main import get_all_ingredients, get_all_recipes


API = Blueprint("API", __name__, url_prefix='/api')


@API.route("recipes/unmade/list-from-file")
def list_unmade():
	# file path is - relative to root? maybe? Yes, it is.

	# note that this will not work currently because I don't have the text file in this directory
	with open("../unmade recipes.txt") as unmade_recipes:
		unmade = unmade_recipes.readlines()

	return render_template("api/list_unmade.html", unmade=unmade)


@API.route("recipes/list")
def list_from_db():
	return encode(get_all_recipes())


@API.route("ingredients/list")
def list_ingredients() -> str:
	return encode(get_all_ingredients())