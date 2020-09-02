from flask import Flask, render_template

newApp = Flask(__name__)

@newApp.route("/")
def myService():
    out = input("enter name: ")
    return render_template("example.html", name = out)
