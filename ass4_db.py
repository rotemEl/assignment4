# a helper mysql database class
import mysql.connector, requests, json, click
from flask import g, current_app
from flask.wrappers import with_appcontext


class DB:
    def __init__(self, host=None, user=None, password=None, database=None):
        if not all([host, user, password, database]):
            self.db = None
            self.cursor = None
            return True

        self.set_object_fields(host, user, password, database)

        if not g.db:
            try:
                g.db = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                )
            except mysql.connector.Error as err:
                print("Failed to connect to MySQL: {}".format(err))
                return False

        self.db = g.db
        self.cursor = self.db.cursor()
        return True

    def set_object_fields(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # db initialization, creation and termination of the database
    def get_db(self):
        if "db" not in g:
            g.db = DB("localhost", "root", "root1234", "assignment4")
            g.db.create_schema()
        return g.db

    def init_db(self):
        db = self.get_db()

        with current_app.open_resource("schema.sql") as f:
            db.executescript(f.read().decode("utf8"))

        return db

    @click.command("init-db")
    @with_appcontext
    def init_db_command(self):
        init_db()
        click.echo("Initialized the database.")

    def close_db(self, e=None):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    # get user from outer source using requests
    def get_outer_source(self):
        url = "https://reqres.in/api/users/"
        ids = self.get_user_ids()
        last_id = ids[-1][0]
        next_id = int(last_id) + 1
        url = url + str(next_id)
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    # get all user ids
    def get_user_ids(self):
        query = "SELECT id FROM users"
        return self.query(query)

    # get list of users in json format from db
    def get_users(self):
        query = "SELECT * FROM users"
        return json.dumps(self.query(query))

    def get_user_by_id(self, id):
        query = "SELECT * FROM users WHERE id = '" + id + "'"
        return self.query(query)

    def get_default_user(self):
        query = "SELECT * FROM users WHERE id = '1'"
        return self.query(query)

    # a method to create intial database and table schema
    def create_schema(self):
        self.create_db()
        self.create_table(
            "users",
            "(id VARCHAR(255), username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))",
        )

    # create db
    def create_db(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.database)
        self.db.commit()

    # create table
    def create_table(self, table, columns):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS " + table + "(" + columns + ")")
        self.db.commit()

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, query):
        self.cursor.execute(query)
        self.db.commit()

    def update(self, query):
        self.cursor.execute(query)
        self.db.commit()

    def delete(self, query):
        self.cursor.execute(query)
        self.db.commit()

    def close(self):
        self.db.close()


db = DB()
