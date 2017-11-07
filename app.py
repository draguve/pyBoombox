import sqlite3 ,os
from flask import Flask, flash, redirect, render_template, request, session, abort , g , url_for , jsonify
app = Flask(__name__)

Database = 'music.db'

#Datebase Access Functions
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(Database)
    return db

def query_db(query, args=(), one=False): #used to retrive values from the table
    conn = get_db()
    cur = conn.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query , args=()): #executes a sql command like alter table and insert
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query , args)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def main():
    genres = query_db("SELECT * FROM genre")
    return render_template('index.html',**locals())

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=80)
