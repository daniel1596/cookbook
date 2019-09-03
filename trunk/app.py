from flask import Flask

from py.blueprints.Api import API
from py.blueprints.Pages import Pages
from py.database.Inserts import insert_all
from py.database.Setup import close_session


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
