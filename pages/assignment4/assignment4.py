# a flask blueprint for the assignment4 page
from flask import Blueprint, render_template, request, redirect, url_for, g
from operator import attrgetter


assignment4 = Blueprint(
    "assignment4",
    __name__,
    static_folder="static",
    static_url_path="/assignment4",
    template_folder="templates",
)


@assignment4.route("/assignment4")
def index():
    db = g.db

    # insert user
    if request.method == "POST":
        id, name, email, passwd = attrgetter("id", "name", "email", "passwd")(
            request.form
        )
        db.insert(
            "INSERT INTO users (id, name, email, passwd) VALUES ('"
            + id
            + "', '"
            + name
            + "', '"
            + email
            + "', '"
            + passwd
            + "')"
        )
        return redirect(url_for("assignment4.assignment4_page"))

    # update user
    if request.method == "PUT":
        id, name, email, passwd = attrgetter("id", "name", "email", "passwd")(
            request.form
        )
        db.update(
            "UPDATE users SET name = '"
            + name
            + "', email = '"
            + email
            + "', passwd = '"
            + passwd
            + "' WHERE id = '"
            + id
            + "'"
        )
        return redirect(url_for("assignment4.assignment4_page"))

    # delete user
    if request.method == "DELETE":
        id = attrgetter("id")(request.form)
        db.delete("DELETE FROM users WHERE id = '" + id + "'")
        return redirect(url_for("assignment4.assignment4_page"))

    # list user
    if request.method == "GET":
        users = db.get_users()
        return render_template("assignment4.html", users=users)
