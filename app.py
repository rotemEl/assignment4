# imports stdlib
from datetime import timedelta
# imports flask
from flask import Flask, jsonify, request, render_template
# imports our code
import ass4_db
from blueprint import assignment4

# app factory
def create_app():
    app = Flask(__name__)
    app.secret_key = "123"

    app.register_blueprint(assignment4)

    app.config["SESSION_PERMANENT"] = True
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=20)

    @app.route("/assignment4/users")
    def get_users():
        return jsonify(ass4_db.get_users())

    @app.route("/assignment4/outer_source", methods=['GET'])
    def outer_source_html():
        return render_template('reqres.html')

    @app.route("/outer_source", methods=['POST'])
    def outer_source():
        _id = request.form["id"]
        res = ass4_db.get_user_from_outer_source(_id)
        return render_template('reqres.html',
                                reqres_user=res)

    @app.route("/assignment4/restapi_users/<int:id>", defaults={"id": 1})
    def restapi_users(id):
        users = ass4_db.get_user_by_id(str(id))

        if users:
            user = users[0]
            return_dict = {
                "name": user.username,
                "email": user.email,

            }
        else:
            return_dict = {"message": "user not found"}

        return jsonify(return_dict)

    return app


    #


    # return app


# run app from cli
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
