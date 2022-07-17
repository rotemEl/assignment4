# a helper mysql database class
import mysql.connector


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
