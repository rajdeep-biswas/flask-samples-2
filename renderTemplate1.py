from flask import Flask, render_template

newApp = Flask(__name__)

@newApp.route("/")
def myService():
    return render_template("example.html")
