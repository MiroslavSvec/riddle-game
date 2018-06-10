## Riddle game

import os
import json
from datetime import datetime
from flask import Flask, redirect, request, render_template, jsonify
import helper

app = Flask(__name__)

""" Riddles Game Setting"""


@app.route('/<user_name>/riddle-g-setting', methods=["GET", "POST"])
def riddle_g_setting(user_name):
	if request.method == "POST":
		profiles_data = helper.read_txt("data/profiles/all-profiles.txt")
		return redirect(f"/{user_name}/riddle-game")
	else:
		profiles_data = helper.read_txt("data/profiles/all-profiles.txt")
		return render_template("riddle-g-setting.html",
                        user_name=user_name, page_title="Riddle Game Setting", profiles=profiles_data)


	


""" Riddle Game """


@app.route('/<user_name>/riddle-game', methods = ["GET", "POST"])
def endless(user_name):
	profiles_data = helper.read_txt("data/profiles/all-profiles.txt")
	return render_template("riddle-game.html",
                        user_name=user_name, page_title="Riddle game", profiles=profiles_data)
