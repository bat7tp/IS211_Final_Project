from flask import Flask, render_template, redirect, request, session, g
import sqlite3 as lite
import sys
import datetime

import os

app = Flask(__name__)

app.secret_key = 'asecretkeythatalmostnobodyknowsss'

def db_connection():
    conn = None
    try:
        conn = lite.connect('the_last_sql_database_final.db')
        print("connected")
    except lite.error as e:
        print(e)
    return conn

def get_username_from_id():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * from users WHERE user_id = ?", [session['user_id']])
    sess_users = cursor.fetchall()
    username = sess_users[0][1]
    print(username)
    cursor.execute("SELECT * from posts WHERE author = ?", [username])
    list_title = cursor.fetchall()
    print(list_title)
    print("successfully received existing posts")
    return list_title

@app.route("/")
def open_post():
    print("in posting fxn")
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * from posts ORDER BY publication_date DESC")
    blog_posts = cursor.fetchall()
    print("successfully posted")
    return render_template('home.html', blog_posts=blog_posts)

@app.route("/dashboard")
def dash():

    if 'user_id' in session:
        got_username = get_username_from_id()

        return render_template("dashboard.html", got_username=got_username)
    else:
        return redirect('/login')

@app.route("/add" , methods = ['POST', 'GET'])
def add():
    return render_template('add.html')

@app.route("/add_submission" , methods = ['POST', 'GET'])
def add_submit():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        print("in method")
        try:
            print("in try")
            title = request.form["book_title"]
            author = request.form["author_name"]
            # author = get_username_from_id()
            content = request.form["content"]
            publication_date = request.form["date"]
            print(title)
            print(author)
            print(content)
            date = datetime.datetime.strptime(publication_date, "%m-%d-%Y").date()
            cursor.execute("INSERT INTO posts (title, author, content, publication_date) VALUES (?, ?, ?, ?)", [title,
                                                                                                    author,
                                                                                                             content,
                                                                                                                date])
            conn.commit()
            print("Title successfully added")


        except lite.Error as e:
            print(e)

    return redirect('/dashboard')


@app.route("/edit/<postid>" , methods = ['POST', 'GET'])
def edit(postid):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * from posts WHERE post_id = ?", [postid])
        post_stuff = cursor.fetchall()[0]

        return render_template("edits.html", post_stuff=post_stuff)

    if request.method == "POST":
        try:
            edited_title = request.form["edit_book_title"]
            edited_author = request.form["edit_author_name"]
            edited_content = request.form["edit_content"]
            edited_date = request.form["edit_date"]

            if edited_date != "":
                cursor.execute("UPDATE posts SET publication_date = ? WHERE post_id = ?", [edited_date, postid])
                conn.commit()
                print(" date Edits successful")

            if edited_content != "":
                cursor.execute("UPDATE posts SET content = ? WHERE post_id = ?", [edited_content, postid])
                conn.commit()
                print("content Edits successful")

            if edited_author != "":
                cursor.execute("UPDATE posts SET author = ? WHERE post_id = ?", [edited_author, postid])
                conn.commit()
                print("author Edits successful")

            if edited_title != "":
                cursor.execute("UPDATE posts SET title = ? WHERE post_id = ?", [edited_title, postid])
                conn.commit()
                print("title Edits successful")

        except lite.Error as err:
            print(err)

    return redirect("/dashboard")


@app.route("/delete/<delid>", methods=['POST', 'GET'])
def delete(delid):
    print("in delete fxn")
    conn = db_connection()
    cursor = conn.cursor()


    if request.method == "POST":
        print("in method")
        try:
            print("in try")
            cursor.execute("DELETE FROM posts WHERE post_id = ?", [delid])
            print(delid)
            conn.commit()
            print("Deletes successful")
        except lite.Error as err:
            print(err)

    return redirect("/dashboard")


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("in login fxn")
    if request.method == 'POST':
        print("one step further in login")
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        conn = db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * from users")
        current_user = cursor.fetchall()

        for user in current_user:
            if user[1] == username and user[2] == password:
                print("work?")
                session['user_id'] = user[0]
                print(session)
                return redirect('/dashboard')
        return redirect('login')


    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)