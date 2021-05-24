import sqlite3 as lite
import sys

con = lite.connect('C:/Users/batsh/Documents/IS 211/IS211_Final_Project/the_last_sql_database_final.db')

with con:
    cur = con.cursor()

    cur.execute(""" CREATE TABLE posts (
                                              post_id integer PRIMARY KEY,
                                                title text NOT NULL,
                                                author text NOT NULL,
                                                content text NOT NULL,
                                                publication_date datetime integer NOT NULL


                                            ); """
                )

    cur.execute(""" CREATE TABLE users (
                                                user_id integer PRIMARY KEY,
                                                  username text NOT NULL,
                                                  password text NOT NULL


                                              ); """
                )

    cur.execute(""" INSERT into users (username, password) VALUES ("Batsheva", "mypassword"), ("John", "notsure")
                                                   


                                                 ; """
                )

