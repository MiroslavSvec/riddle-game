import os
import json
from datetime import datetime
from random import shuffle 
from flask import Flask, redirect, request, render_template, jsonify

app = Flask(__name__)

""" Helper functions """

def write_to_txt(filename, write_mode, data):
    with open(filename, f"{write_mode}") as file:
        file.writelines(data)


def write_to_json(filename, write_mode, data):
    with open(f'{filename}', f'{write_mode}') as outfile:
   		json.dump(data, outfile)

def read_txt(filename):
	with open(f'{filename}', "r") as file:
		data = file.readlines()
		return data


def read_json(filename):
	with open(f'{filename}', "r") as file:
		data = json.load(file)
		return data

def get_profile_data(user_name):
	all_profiles = read_txt('data/profiles/all-profiles.txt')
	for profile in all_profiles:
		if profile.strip('\n') == user_name:
			profile = read_json(f"data/profiles/{user_name}.json")
			return jsonify(profile)


def post_profile_data(user_name):
	profile = get_profile_data(user_name)
	if profile:
		return jsonify(user_name)
	else:
		profile_created = datetime.now().strftime("%H:%M:%S")
		profiles = {}
		profiles[f'{user_name}'] = []
		profiles[f'{user_name}'].append(
                    {'name': f'{user_name}',
					'login': "true",
                     'created': f'{profile_created}',
                     'score': 0,
                     'right_answers': 0,
                     'wrong_answers': 0,
                     'skipped_questions': 0,
                     })		
		app_data = read_json('data/app_data.json')
		members_count = app_data['1.0'][0]["members"]
		app_data['1.0'][0]["members"] = members_count +1

		write_to_json("data/app_data.json", "w", app_data)
		write_to_json(f"data/profiles/{user_name}.json", "w", profiles)
		write_to_txt(f"data/profiles/all-profiles.txt",
                    "a", f"{user_name}" + '\n')

		return jsonify({'status': "success"}, {'profile': f"{user_name}"})



""" Rest API """


@app.route('/<user_name>/data', methods=["GET"])
def get(user_name):
	return get_profile_data(user_name)


@app.route('/<user_name>/data', methods=["POST"])
def post(user_name):
	return post_profile_data(user_name)
		
@app.route('/app_data')
def get_app_data():
	app_data = read_json('data/app_data.json')
	return jsonify(app_data)
	

""" Create profile page """


@app.route('/')
def index():
	app_data = read_json('data/app_data.json')
	app_data = app_data['1.0'][0]["members"]
	## Render index.html by default
	return render_template("index.html", members=app_data)


""" Profile page """

@app.route('/<user_name>')
def profile_page(user_name):
	## Get profile data
	profiles_data = read_txt("data/profiles/all-profiles.txt")
	## Check if there is more then one profile
	if len(profiles_data) > 0:
		return render_template("profile.html",
                         user_name=user_name, page_title=f"{user_name}" + " profile", profiles=profiles_data)
	## Render default template
	return render_template("profile.html",
                        user_name=user_name, page_title=f"{user_name}" + " profile")


""" Riddles Game Setting"""


@app.route('/<user_name>/riddle-g-setting', methods=["GET", "POST"])
def riddle_g_setting(user_name):
	if request.method == "POST":
		profiles_data = read_txt("data/profiles/all-profiles.txt")
		return redirect(f"/{user_name}/riddle-game")
	else:
		profiles_data = read_txt("data/profiles/all-profiles.txt")
		return render_template("riddle-g-setting.html",
                        user_name=user_name, page_title="Riddle Game Setting", profiles=profiles_data)


	


""" Riddle Game """


@app.route('/<user_name>/riddle-game', methods = ["GET", "POST"])
def endless(user_name):
	profiles_data = read_txt("data/profiles/all-profiles.txt")
	return render_template("riddle-game.html",
                        user_name=user_name, page_title="Riddle game", profiles=profiles_data)



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
