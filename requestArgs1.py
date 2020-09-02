from flask import Flask, render_template, request

newApp = Flask(__name__)

@newApp.route("/")
def myService():
    out = request.args.get("name")
    return render_template("example.html", name = out)
