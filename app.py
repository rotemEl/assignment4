# imports
from flask import Flask, g
from pages.assignment4.assignment4 import assignment4_page
from db import DB

# app
app = Flask(__name__)
app.register_blueprint(assignment4_page)

# db
if 'db' not in g:
    g.db = DB('localhost', 'root', 'sana1984', 'assignment4')
    g.db.create_schema()

db = g.db

# run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



