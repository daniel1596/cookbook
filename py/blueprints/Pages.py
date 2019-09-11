from flask import Blueprint, render_template

from py.Config import Config
from py.database.Queries import get_recipe_by_name


Pages = Blueprint("Pages", __name__)


@Pages.route("/")
def index():
	return __render_with_vue("index.html")


@Pages.route("/recipes/<name>")
def recipe_detail(name: str):
	recipe = get_recipe_by_name(name)
	return __render_with_vue("recipe_detail.html", recipe=recipe)


def __render_with_vue(path: str, **kwargs):
	return render_template(path, vue_file=Config.vue_file, **kwargs)
