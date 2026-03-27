from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="school"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    db.commit()
    return redirect('/students')


@app.route('/students')
def students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template("student.html", students=data)


app.run(debug=True)
