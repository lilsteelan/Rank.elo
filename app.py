from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "page is functional"


@app.route('/add')
def add():
    return render_template("createobject.html")