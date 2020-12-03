from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story as story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/questions")
def show_questions():
    """ Shows the form that requires inputs needed to create
    story instance """

    form_inputs = story.prompts

    return render_template("questions.html", prompts=form_inputs)


@app.route("/story")
def make_story():
    """ Create a story page from user input on /questions """

    user_input = {key: request.args[key] for key in request.args.keys()}
    text = story.generate(user_input)

    return render_template('story.html', user_story=text)
