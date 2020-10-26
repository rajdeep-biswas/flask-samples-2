from flask import Flask, render_template, request, redirect
import json

newApp = Flask(__name__)

jsonfilename = 'chatter.json'

def write_json(data, filename): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

@newApp.route("/")
def myService():
	with open(jsonfilename, 'r') as openfile:
		jsonObject = json.load(openfile)
	return render_template("example.html", messages = jsonObject["messages"])

@newApp.route("/postMessage", methods = ["POST"])
def postMessage():

	if request.form['name'] and request.form['message']:
		newMessage = {
			"name": request.form['name'],
			"message": request.form['message']
		}

		with open(jsonfilename) as json_file: 
			data = json.load(json_file)
			temp = data['messages']
			temp.append(newMessage)

		write_json(data, jsonfilename)
		
	return redirect("/")
