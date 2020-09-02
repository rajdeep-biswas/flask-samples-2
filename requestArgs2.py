from flask import Flask, render_template, request

newApp = Flask(__name__)

@newApp.route("/")
def myService():
    out = request.args.get("name")
    if not out:
        out = "i feel godlike because this works"
    return render_template("example.html", name = out)
