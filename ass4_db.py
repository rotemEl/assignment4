# a helper mysql database class
import mysql.connector, requests, json, click
from flask import g, current_app, jsonify
from flask.cli import with_appcontext
from operator import attrgetter


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(
        host="localhost", user="root", passwd="root1234", database="myflaskappdb"
    )
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query, query_type='')
    #

    if query_type == "commit":
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        return_value = connection.commit()

    if query_type == "fetch":
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        return_value = cursor.fetchall()

    connection.close()
    cursor.close()
    return return_value


def _connect(cfg):
    return mysql.connector.connect(
        attrgetter("host", "user", "passwd", "db_name")(cfg)
    )


def _create_schema_with_data(conn):
    with current_app.open_resource("schema.sql") as f:
        conn.executescript(f.read().decode("utf8"))


def get_user_from_outer_source():
    url = "https://reqres.in/api/users/",

    response = requests.get(url)

    return response.json()


def get_users():
    query = "SELECT * FROM users"
    return jsonify(interact_db(query, query_type='fetch'))


def get_user_by_id(id):
    query = "SELECT * FROM users WHERE id = '" + id + "'"
    return jsonify(interact_db(query, query_type='fetch'))


def insert_user(name, email, passwd):
    query = "INSERT INTO users(name, email, passwd) VALUES ('%s', '%s', '%s')" % (
        name,
        email,
        passwd,
    )

    return interact_db(query, query_type='commit')

def update_user(id, name, email, passwd):
    query = "UPDATE users SET name = '%s', email = '%s', passwd = '%s' WHERE id = '%s'" % (
        name,
        email,
        passwd,
        id,
    )

    return interact_db(query, query_type='commit')

def delete_user(id):
    query = "DELETE FROM users WHERE id = '%s'" % id

    return interact_db(query, query_type='commit')


