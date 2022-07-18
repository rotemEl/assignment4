# a flask blueprint for the assignment4 page
from flask import Blueprint, render_template, request, redirect, url_for, g
from operator import attrgetter


assignment4 = Blueprint('assignment4', __name__, static_folder='static', static_url_path='/assignment4',
                        template_folder='templates')


@assignment4.route('/assignment4')
def index():
    # if request method is post then get id (default null), 
    # name, email and passwd from form and insert into database
    db = g.db

    # insert user
    if request.method == 'POST':
        id, name, email, passwd
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        passwd = request.form['passwd']
        # insert into database
        db.insert("INSERT INTO users (id, name, email, passwd) VALUES ('" + id + "', '" + name + "', '" + email + "', '" + passwd + "')")
        # redirect to assignment4 page
        return redirect(url_for('assignment4.assignment4_page'))

    # update user
    if request.method == 'PUT':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        passwd = request.form['passwd']

        db.update("UPDATE users SET name = '" + name + "', email = '" + email + "', passwd = '" + passwd + "' WHERE id = '" + id + "'")
        return redirect(url_for('assignment4.assignment4_page'))

    # delete user
    if request.method == 'DELETE':
        id = request.form['id']
        # delete from database
        db.delete("DELETE FROM users WHERE id = '" + id + "'")
        # redirect to assignment4 page
        return redirect(url_for('assignment4.assignment4_page'))

    # list user
    if request.method == 'GET':
        users = db.get_users()
        return render_template('assignment4.html', users=users)
