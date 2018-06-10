import os
import json
from datetime import datetime
from random import shuffle 
from flask import Flask, redirect, request, render_template, jsonify

## Custom .py
import riddle
import helper

app = Flask(__name__)


""" Rest API """


@app.route('/<user_name>/data', methods=["GET"])
def get(user_name):
	return helper.read_json(user_name)


@app.route('/<user_name>/data', methods=["POST"])
def post(user_name):
	return helper.create_profile_data(user_name)
		
@app.route('/app_data')
def get_app_data():
	app_data = helper.read_json('data/app_data.json')
	return jsonify(app_data)
	

""" Create profile page """


@app.route('/')
def index():
	app_data = helper.read_json('data/app_data.json')
	app_data = app_data['1.0'][0]["members"]
	## Render index.html by default
	return render_template("index.html", members=app_data)


""" Profile page """

@app.route('/<user_name>')
def profile_page(user_name):
	## Get profile data
	profiles_data = helper.read_txt("data/profiles/all-profiles.txt")
	## Check if there is more then one profile
	if len(profiles_data) > 0:
		return render_template("profile.html",
                         user_name=user_name, page_title=f"{user_name}" + " profile", profiles=profiles_data)
	## Render default template
	return render_template("profile.html",
                        user_name=user_name, page_title=f"{user_name}" + " profile")






""" Chat in separate page """

@app.route('/chat')
def chat():
	return render_template("chat.html")


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)

""" Create 404 page and 500 error """
""" Categories for questions """
""" Score """
""" Limit wrong answers """
""" Add riddle """
""" Profiles """
""" Passwords """
""" View Friends """
""" Chat / Password / Send Invitaiton / """
