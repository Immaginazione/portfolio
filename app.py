from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about-me")
def about():
    return render_template("about-me.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")