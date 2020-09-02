from flask import Flask

newApp = Flask(__name__)

@newApp.route("/")
def myService():
    return "hello, world"
