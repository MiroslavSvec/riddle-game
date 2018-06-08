import os
import json
from datetime import datetime
from random import shuffle 
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

def read_txt(filename):
	with open(f'{filename}', "r") as file:
		data = file.readlines()
		return data


def read_json(filename):
	with open(f'{filename}', "r") as file:
		data = json.load(file)
		return data



""" Create profile page """


@app.route('/', methods=["GET", "POST"])
def index():
		## Create Profiles and store them in .json (as profile data) and .txt (append to profiles list)
	if request.method == "POST":
		profile_name = request.form["username"]
		with open('data/profiles/all-profiles.txt', 'r') as file:
			data = file.readlines()
			for profile in data:
				if profile.strip('\n') == profile_name:
					return render_template("index.html")
			profile_created = datetime.now().strftime("%H:%M:%S")
			profiles = {}
			profiles[f'{profile_name}'] = []
			profiles[f'{profile_name}'].append(
                                          {'name': f'{profile_name}',
                                             'created': f'{profile_created}',
                                             'score': 0,
                                             'right_answers': 0,
                                             'wrong_answers': 0,
                                             'skipped_questions': 0,
                                             })
			write_to_json(f"data/profiles/{profile_name}.json", "w", profiles)
			write_to_txt(f"data/profiles/all-profiles.txt",
					             "a", f"{profile_name}" + '\n')
			## Redirect user to profile page
			return redirect(profile_name)
	## Render index.html by default
	return render_template("index.html")


""" Profile page """

@app.route('/<user_name>')
def profile_page(user_name):
	## Get profile data
	profiles_data = read_txt(f"data/profiles/all-profiles.txt")
	## Check if there is more then one profile
	if len(profiles_data) > 0:
		return render_template("profile.html",
                         user_name=user_name, page_title=f"{user_name}" + " profile", profiles=profiles_data)
	## Render default template
	return render_template("profile.html",
                        user_name=user_name, page_title=f"{user_name}" + " profile")

""" Login page """

@app.route('/<user_name>/login')
def login(user_name):
	return render_template("login.html",
                        user_name=user_name, page_title=f"{user_name}" + " profile	")


""" Riddles Game Setting"""


@app.route('/<user_name>/riddle-g-setting', methods=["GET", "POST"])
def riddle(user_name):
	profiles_data = read_txt(f"data/profiles/all-profiles.txt")
	return render_template("riddle-g-setting.html",
                        user_name=user_name, page_title="Riddle Game Setting", profiles=profiles_data)


""" Riddles Game """


@app.route('/<user_name>/riddle-game', methods=["GET", "POST"])
def funcname(user_name):
	profiles_data = read_txt(f"data/profiles/all-profiles.txt")
	return render_template("riddle-game.html",
                        user_name=user_name, page_title="Riddle Game", profiles=profiles_data)



""" Chat in separate page """

@app.route('/<user_name>/chat')
def chat(user_name):
	return render_template("chat.html", user_name=user_name)


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
