# a helper mysql database class
import mysql.connector
import requests

class DB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()

    # get user from outer source using fetch api
    def get_outer_source(self):
        # get user from outer source
        url = 'https://reqres.in/api/users/'
        # get all ids from db
        ids = self.get_user_ids()
        # get the last id from db
        last_id = ids[-1][0]
        # get the next id from outer source
        next_id = int(last_id) + 1
        # add next id to url
        url = url + str(next_id)
        response = requests.get(url)
        # convert to json
        data = json.loads(response.text)
        # get user from outer source
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
        # create database
        self.create_db()

        # create table
        self.create_table("users", "(id VARCHAR(255), username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

    # create db
    def create_db(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.database)
        self.db.commit()

    # create table
    def create_table(self, table, columns):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS " +
                            table + "(" + columns + ")")
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
