from flask import Flask, render_template
from webbrowser import open

from blueprints.Api import API
from blueprints.Pages import Pages
from database.Inserts import insert_all
from database.Main import get_recipe_by_name
from database.Setup import close_session


app = Flask(__name__)
app.register_blueprint(API)
app.register_blueprint(Pages)


def main():
	insert_all()
	
	#open("127.0.0.1:5000")
	app.run(debug=True)

	# Is this being hit? And will the session be auto-closed anyway? I don't know.
	close_session()


if __name__ == "__main__":
	main()
