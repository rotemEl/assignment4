# imports stdlib
import json
from datetime import timedelta


# imports flask
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


# imports our code
from pages.assignment4.assignment4 import assignment4


def create_app():
    app = Flask(__name__)
    app.secret_key = "123"

    app.register_blueprint(assignment4)

    from flask_debugtoolbar import DebugToolbarExtension

    toolbar = DebugToolbarExtension(app)

    with app.app_context():
        from ass4_db import dbh
        db = dbh.get_db()

    app.config["SESSION_PERMANENT"] = True
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=20)

    # routes
    @app.route("/assignment4/users")
    def get_users():
        return db.get_users()

    @app.route("/assignment4/outer_source")
    def get_outer_source():
        return db.get_outer_source()

    @app.route("/assignment4/restapi_users/<id>", methods=["POST"])
    def restapi_users(id):
        if not id:
            return db.get_default_user()
        if id is not int:
            return json.dumps({"error": "id must be an integer"})
        return db.get_user_by_id(id)

    return app


# run app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
