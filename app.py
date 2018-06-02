import os
import json
from datetime import datetime
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

""" Write to file """

def write_to_txt(filename, write_mode, data):
    with open(filename, f"{write_mode}") as file:
        file.writelines(data)


def write_to_json(filename, write_mode, data):
    with open(f'{filename}', f'{write_mode}') as outfile:
   		json.dump(data, outfile)

""" Read data """

def read_data(filename):
	data = []
	with open(f'{filename}', "r") as file:
		data = file.readlines()
		return data

""" Login page """

@app.route('/', methods=["GET", "POST"])
def index():	
	## Need to fix bug with all user using same profile
	""" with open("data/profiles.txt", "r") as x:
		profile = x.readlines()
		if profile:
			return redirect(f"/{profile[0]}" """
	## Create Profiles and store them in .json and .txt
	if request.method == "POST":
		profile_name = request.form["username"]
		profile_created = datetime.now().strftime("%H:%M:%S")
		profiles = {}
		profiles[f'{profile_name}'] = []
		profiles[f'{profile_name}'].append(
                    {'name': f'{profile_name}', 
					'created': f'{profile_created}', 
					'score': 0,
					'right_answers': 0,
					'wrong_answers': 0
					})
		write_to_json(f"data/profiles/{profile_name}.json", "w", profiles)
		write_to_txt("data/profiles/all-profiles.txt", "a", f"{profile_name}" + '\n')
		## Redirect user to profile page
		return redirect(profile_name)
	## Render index.html by default
	return render_template("index.html")

""" Profile page """

@app.route('/<user_name>')
def profile_page(user_name):
	## Get profile data
	profiles = read_data("data/profiles/all-profiles.txt")
	## Check if there is more then one profile
	if len(profiles) > 0:
		return render_template("profile.html",
                          		user_name=user_name, page_title=f"{user_name}" + " Profile", profiles=profiles)
	## Render default template
	return render_template("profile.html",
                        	user_name=user_name, page_title=f"{user_name}" + " Profile")

""" Riddles Game """

@app.route('/<user_name>/riddle')
def riddle(user_name):
	profiles = read_data("data/profiles/all-profiles.txt")
	return render_template("riddles.html", 
							user_name=user_name, page_title="Riddle Game", profiles=profiles)

""" Chat in separate page """

@app.route('/<user_name>/chat')
def chat(user_name):
	return render_template("chat.html", user_name=user_name)


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
