# imports stdlib
import click
from datetime import timedelta


# imports flask
from flask import Flask, current_app, g
from flask.cli import with_appcontext
from flask_debugtoolbar import DebugToolbarExtension


# imports our code
from ass4_db import DB
from pages.assignment4.assignment4 import assignment4


# db initialization and creation
def get_db():
    if 'db' not in g:
        g.db = DB('localhost', 'root', 'root1234', 'assignment4')
        g.db.create_schema()
    return g.db     


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    return db


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def create_app():
    app = Flask(__name__)
    app.secret_key = '123'
    
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)
    
    db = get_db()

    app.config['SESSION_PERMANENT'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

    # routes 
    @app.route('/assignment4/users')
    def get_users():
        return db.get_users()

    @app.route('/assignment4/outer_source')
    def get_outer_source():
        return db.get_outer_source()

    @app.route('/assignment4/restapi_users/<id>', methods=['POST'])
    def restapi_users(id):
        if not id:
            return db.get_default_user()
        if id is not int: return json.dumps({'error': 'id must be an integer'})
        return db.get_user_by_id(id)
    
    return app

# run app
if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(assignment4)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
