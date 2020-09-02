from flask import Flask

newApp = Flask(__name__)

@newApp.route("/")
def myService():
    f = open('templates/example.html', 'r')
    f = f.read()
    return f;
