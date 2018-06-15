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
## {answer: "test answer"}

## {
##	"game": [
##		{
##			"player_name": "test",
##			"game_started": "00:43:17",
##			"categories": "all",
##			"mods": "none",
##			"tries": "1",
##			"result": "",
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
         'result': "",
         'score': 0,
         'right_answers': 0,
         'wrong_answers': 0,
         'skipped_questions': 0,
         })
	# Create Game folder
    os.makedirs(f"data/profiles/{profile_name}/riddle_game")
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
    random.shuffle(questions["questions"])
	# Pick question from the database
    riddle_game_data["game"][0]["question"] = pick_question(questions)
	# Write data
    helper.write_to_txt(f"data/riddle-game/all-players.txt",
                        "a", f"{profile_name}" + '\n')	
    helper.write_to_json(
        f"data/profiles/{profile_name}/riddle_game/player_{profile_name}.json", "w", riddle_game_data)
    helper.write_to_json(
	    f"data/profiles/{profile_name}/riddle_game/questions.json", "w", questions)
    return jsonify(riddle_game_data)


def pick_question(questions):
	question = questions["questions"][0]["riddle"]	
	return question



def riddle_game(user_name):
	questions = helper.read_json(
	    f"data/profiles/{user_name}/riddle_game/questions.json")
	profile = helper.read_json(
	    f"data/profiles/{user_name}/riddle_game/player_{user_name}.json")
	data = request.get_json(force=True)
	## Format both user as well as correct answer
	correct_answer = questions["questions"][0]["answer"]
	correct_answer = correct_answer.lower()
	correct_answer = "".join(correct_answer.split())
	user_answer = data["answer"]
	user_answer = "".join(user_answer.split())
	user_answer = user_answer.lower()

	
	if user_answer == correct_answer:
		profile["game"][0]["right_answers"] += 1
		profile["game"][0]["result"] = "Correct"
		helper.write_to_json(
            f"data/profiles/{user_name}/riddle_game/player_{user_name}.json", "w", profile)
		return profile
	else:
		profile["game"][0]["wrong_answers"] += 1
		profile["game"][0]["result"] = "Wrong"
		helper.write_to_json(
                    f"data/profiles/{user_name}/riddle_game/player_{user_name}.json", "w", profile)
		return profile
	print(correct_answer)
	print(user_answer)
	print(profile)


	return correct_answer



