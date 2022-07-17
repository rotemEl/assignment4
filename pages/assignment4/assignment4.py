# a flask blueprint for the assignment4 page
from flask import Blueprint, render_template, request, redirect, url_for, g


assignment4 = Blueprint('assignment4', __name__)


@assignment4.route('/assignment4')
def assignment4_page():
    # if request method is post
    # then get id (default null), username, email and password from form
    # and insert into database
    db = g.db
    if request.method == 'POST':
        id = request.form['id']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # insert into database
        db.insert("INSERT INTO users (id, username, email, password) VALUES ('" + id + "', '" + username + "', '" + email + "', '" + password + "')")
        # redirect to assignment4 page
        return redirect(url_for('assignment4.assignment4_page'))

    return render_template('assignment4.html')
