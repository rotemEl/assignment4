# a helper mysql database class
import mysql.connector, requests, json, click
from flask import g, current_app
from flask.cli import with_appcontext
from operator import attrgetter


class DB:
    def __init__(self, host=None, user=None, passwd=None, database=None):
        self.set_db_connection_fields(host, user, passwd, database)

        if not g.db:
            if not all([self.host, self.user, self.passwd, self.db_name]):
                g.db, self.db, self.cursor = None
            else:
                try:
                    g.db = self._connect()
                except mysql.connector.Error as err:
                    print("Failed to connect to MySQL: {}".format(err))
                    return False

        self.db = g.db
        self.cursor = self.db.cursor()
        self.init_db()
        return True

    def set_db_connection_fields(
        self, host=None, user=None, passwd=None, database=None
    ):
        self.host, self.user, self.passwd, self.db_name = host, user, passwd, database

    def _connect(self):
        if not all([self.host, self.user, self.passwd, self.db_name]):
            return False

        return mysql.connector.connect(
            attrgetter("host", "user", "passwd", "db_name")(self)
        )

    def _create_schema(self):
        with current_app.open_resource("schema.sql") as f:
            self.db.executescript(f.read().decode("utf8"))

    def init_db(self):
        if g.db:
            self._create_schema()
            return True

        if not self.db:
            self.db = self._connect()
            if self.db:
                self.cursor = self.db.cursor()

        self._create_schema()
        g.db = self.db

        return True

    @click.command("init-db")
    @with_appcontext
    def init_db_command(self):
        self.init_db()
        click.echo("Initialized the database.")

    def close_db(self, e=None):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    # get user from outer source using requests
    def get_outer_source(self):
        url, ids, last_id, next_id = (
            "https://reqres.in/api/users/",
            self.get_user_ids(),
            ids[-1][0],
            int(last_id) + 1,
        )
        url = url + str(next_id)
        response = requests.get(url)

        return json.loads(response.text)

    def get_user_ids(self):
        query = "SELECT id FROM users"
        return self.query(query)

    def get_users(self):
        query = "SELECT * FROM users"
        return json.dumps(self.query(query))

    def get_user_by_id(self, id):
        query = "SELECT * FROM users WHERE id = '" + id + "'"
        return self.query(query)

    def get_default_user(self):
        query = "SELECT * FROM users WHERE id = '1'"
        return self.query(query)

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
