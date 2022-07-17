# a flask blueprint for the assignment4 page
from flask import Blueprint, render_template, request, redirect, url_for, g


assignment4 = Blueprint('assignment4', __name__, static_folder='static', static_url_path='/assignment4',
                        template_folder='templates')


@assignment4.route('/assignment4')
def index():
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
    if request.method == 'PUT':
        id = request.form['id']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # update database
        db.update("UPDATE users SET username = '" + username + "', email = '" + email + "', password = '" + password + "' WHERE id = '" + id + "'")
        # redirect to assignment4 page
        return redirect(url_for('assignment4.assignment4_page'))
    if request.method == 'DELETE':
        id = request.form['id']
        # delete from database
        db.delete("DELETE FROM users WHERE id = '" + id + "'")
        # redirect to assignment4 page
        return redirect(url_for('assignment4.assignment4_page'))
    # if request method is get
    # then get all users from database
    # and render template
    if request.method == 'GET':
        users = db.get_users()
        return render_template('assignment4.html', users=users)
