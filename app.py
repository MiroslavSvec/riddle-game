import os
from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

""" Categories for questions """
""" Score """
""" Limit wrong answers """
""" Add riddle """
""" Profiles """
""" Chat / Password / Send Invitaiton """


if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=True)
