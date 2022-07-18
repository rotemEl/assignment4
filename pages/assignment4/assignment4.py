# imports
from operator import attrgetter
from flask import Blueprint, g, redirect, render_template, request, url_for

# blue print
assignment4 = Blueprint(
    "assignment4",
    __name__,
    static_folder="static",
    static_url_path="/assignment4",
    template_folder="templates",
)


# routes
@assignment4.route("/assignment4")
def index():
    from ass4_db import dbh
    if not dbh.get("db", None):
        dbh.init_db()
    if g.get("db", None):
        db = g.db
    else:
        db = db.get_db()

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
