import os
import json
from datetime import datetime
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

## Write to file
def write_to_txt(filename, write_mode, data):
    with open(filename, f"{write_mode}") as file:
        file.writelines(data)


def write_to_json(filename, write_mode, data):
    with open(f'{filename}', f'{write_mode}') as outfile:
   		json.dump(data, outfile)

## Login page
@app.route('/', methods=["GET", "POST"])
def index():	
	## Need to fix bug with all user using same profile
	""" with open("data/profiles.txt", "r") as x:
		profile = x.readlines()
		if profile:
			return redirect(f"/{profile[0]}" """
	## Create Profiles and store them in .json and .csv
	if request.method == "POST":
		profile_name = request.form["username"]
		profile_created = datetime.now().strftime("%H:%M:%S")
		profiles = {}
		profiles[f'{profile_name}'] = []
		profiles[f'{profile_name}'].append(
                    {'name': f'{profile_name}', 'created': f'{profile_created}', 'score': 0})
		write_to_json(f"data/profiles/{profile_name}.json", "w", profiles)
		write_to_txt("data/profiles/all-profiles.csv", "a", f"{profile_name + ','}")
		## Redirect user to profile page
		return redirect(request.form["username"])
	## Render index.html by default
	return render_template("index.html")

## Profile page
@app.route('/<user>')
def profile_page(user):
	return render_template("profile.html")
## Games
@app.route('/<user>/games')
def games():
	return render_template("games.html")
## Chat in separate page
@app.route('/<user>/chat')
def chat(user):
	return render_template("chat.html")


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)


""" Categories for questions """
""" Score """
""" Limit wrong answers """
""" Add riddle """
""" Profiles """
""" Passwords """
""" View Friends """
""" Chat / Password / Send Invitaiton / """
