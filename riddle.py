# Riddle game

import os
import json
import random
from datetime import datetime
from shutil import copyfile
from flask import Flask, redirect, request, render_template, jsonify

## Custom .py
import helper


app = Flask(__name__)


""" Data Sample """

## {"riddle_game_data":{"id":"test","categories":"all","mods":"none","tries":"1"}}

## {
##	"test": [
##		{
##			"player_name": "test",
##			"game_started": "00:43:17",
##			"categories": "all",
##			"mods": "none",
##			"tries": "1",
##			"score": 0,
##			"right_answers": 0,
##			"wrong_answers": 0,
##			"skipped_questions": 0
##		}
##	]
##}



""" Riddles Game Setting"""


def riddle_g_setting(user_name):
    if request.method == "POST":
        profiles_data = helper.read_txt("data/profiles/all-profiles.txt")
        return redirect(f"/{user_name}/riddle-game")
    else:
        profiles_data = helper.read_txt("data/profiles/all-profiles.txt")
        return render_template("riddle-g-setting.html",
                               user_name=user_name, page_title="Riddle Game Setting", profiles=profiles_data)


""" Riddle Game """


def create_riddle_game(data):
	# Profile data
    game_created = datetime.now().strftime("%H:%M:%S")
    profile_name = data["riddle_game_data"]["id"]
	## Coment should put it to separate file 
    riddle_game_data = {}
    riddle_game_data["game"] = []
    riddle_game_data["game"].append(
        {'player_name': f'{profile_name}',
         'game_started': f'{game_created}',
         'categories': f"{data['riddle_game_data']['categories']}",
         'mods': f"{data['riddle_game_data']['mods']}",
         'tries': f"{data['riddle_game_data']['tries']}",
         'question': [],
         'answer': [],
         'score': 0,
         'right_answers': 0,
         'wrong_answers': 0,
         'skipped_questions': 0,
         })
	# Write data
    helper.write_to_txt(f"data/riddle-game/all-players.txt",
                        "a", f"{profile_name}" + '\n')	
    os.makedirs(f"data/profiles/{profile_name}/riddle_game")
    helper.write_to_json(
        f"data/profiles/{profile_name}/riddle_game/player_{profile_name}.json", "w", riddle_game_data)
    ## Comment: Need to add error statment / add user questions
	# Copy question file to work with fresh file
    if riddle_game_data["game"][0]["categories"] == "all":
        copyfile("data/riddle-game/all.json",
                 f"data/profiles/{profile_name}/riddle_game/questions.json")
    elif riddle_game_data["game"][0]["categories"] == "general":
        copyfile("data/riddle-game/general.json",
                 f"data/profiles/{profile_name}/riddle_game/questions.json")
    else:
        copyfile("data/riddle-game/mixed.json",
                 f"data/profiles/{profile_name}/riddle_game/questions.json")

	## To shuffle the questions that every game is different
    questions = helper.read_json(
        f"data/profiles/{profile_name}/riddle_game/questions.json")
    random.shuffle(questions["all"])
    helper.write_to_json(
	    f"data/profiles/{profile_name}/riddle_game/questions.json", "w", questions)
    return jsonify(riddle_game_data)


def riddle_game(user_name):
	data = request.get_json(force=True)
	tries = data['riddle_game_data']['tries']
	right_answers = data['riddle_game_data']['right_answers']
	wrong_answers = data['riddle_game_data']['wrong_answers']
	skipped_questions = data['riddle_game_data']['skipped_questions']
	question_result = []

	with open(f"data/profiles/{user_name}/riddle_game/player_{user_name}.json", "r") as file:
		game_data = json.load(file)
		question_result = game_data
