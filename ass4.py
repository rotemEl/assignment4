# imports stdlib
from datetime import timedelta


# imports flask
from flask import Flask, jsonify


# imports our code
from pages.assignment4.assignment4 import assignment4

# app factory
def create_app():
    app = Flask(__name__)
    app.secret_key = "123"

    app.register_blueprint(assignment4)

    app.config["SESSION_PERMANENT"] = True
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=20)

    from ass4_db import (
        get_users,
        get_user_from_outer_source,
        get_user_by_id,
        insert_user,
        update_user,
        delete_user,
        interact_db,
    )

    # routes
    @app.route("/assignment4/users")
    def get_users():
        return get_users()

    @app.route("/assignment4/outer_source")
    def outer_source():
        return get_user_from_outer_source()

    @app.route("/assignment4/restapi_users/<int:id>", defaults={"id": -1})
    def restapi_users(id):
        query = f"select * from users where id={id}"
        users_list = interact_db(query, query_type="fetch")

        if len(users_list) == 0:
            return_dict = {"message": "user not found"}
        else:
            user_list = users_list[0]
            return_dict = {
                "name": user_list.name,
                "email": user_list.email,
                "create_date": user_list.create_date,
            }

        return jsonify(return_dict)

    return app


# run app from cli
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
