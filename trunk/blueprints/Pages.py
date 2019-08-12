from flask import Blueprint, render_template
#from jsonpickle import encode

from database.Main import get_recipe_by_name


Pages = Blueprint("Pages", __name__)


@Pages.route("/")
def index():
	return render_template("index.html")

	
@Pages.route("/recipes/<name>")
def recipe_detail(name: str):
	recipe = get_recipe_by_name(name)
	return render_template("recipe_detail.html", recipe=recipe)