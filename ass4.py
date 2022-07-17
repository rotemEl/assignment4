# imports
from flask import Flask, g
from pages.assignment4.assignment4 import assignment4
from db import DB

# app
app = Flask(__name__)
app.register_blueprint(assignment4)

# db
if 'db' not in g:
    g.db = DB('localhost', 'root', 'sana1984', 'assignment4')
    g.db.create_schema()
    db = g.db
    
# routes 
@app.route('/assignment4/users')
def get_users():
    return db.get_users()

@app.route('/assignment4/outer_source')
def get_outer_source():
    return db.get_outer_source()

@app.route('/assignment4/restapi_users/<id>', methods=['POST'])
def restapi_users(id):
    # if no id was given, then get a default user from db
    if not id:
        return db.get_default_user()
    # use int validation on id
    if id is not int: return json.dumps({'error': 'id must be an integer'})
    # get user from db by id
    return db.get_user_by_id(id)
# run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




