import os
import json
from flask import Flask, redirect, render_template

app = Flask(__name__)

## Get Profiles

def get_profile_data():
	profiles = []
	with open('data/profiles.txt', 'r') as profile_data:
		profiles = profile_data.readlines()
		print(profiles)
	return profiles

@app.route('/')
def index():
	return render_template("profile-page.html")

""" Categories for questions """
""" Score """
""" Limit wrong answers """
""" Add riddle """
""" Profiles """
""" View Friends """
""" Chat / Password / Send Invitaiton / """

@app.route('/<user>')
def chat(user):
	return render_template("chat.html")
## Chat in separate window 

if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)
