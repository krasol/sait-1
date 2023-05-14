from flask import Flask, render_template, request
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from db.sql import add

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('site.html')


@app.route('/reg_run', methods=['POST', 'GET'])
def reg_run():
    a = request.form['name']
    a1 = request.form['fname']
    a2 = request.form['nomer']
    a3 = request.form['pochta']
    a4 = request.form['nisha']
    s = a + " " + a1 + " " + a2 + " " + a3 + " " + a4
    add(s)
    return render_template("site.html")


def add(item):
    connect = sqlite3.connect("db/database.db")
    cursor = connect.cursor()
    m = []
    m.append(item)
    cursor.execute('INSERT INTO user (users) VALUES(?)', m)
    connect.commit()
    cursor.close()


if __name__ == "__main__":
    app.run()
