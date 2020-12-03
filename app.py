from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def pick_a_story():
    """ Shows a dropdown list for user to select a story """

    return render_template("home.html", story_options=stories.story_list)


@app.route("/questions")
def show_questions():
    """ Shows the form that requires inputs needed to create
    story instance """

    story_name = request.args["selected"]
    form_inputs = stories.story_list[story_name].prompts

    return render_template("questions.html",
                           selected_story=story_name,
                           prompts=form_inputs)


@app.route("/story/<selected_story>")
def make_story(selected_story):
    """ Create a story page from user input on /questions """

    user_input = request.args
    story_instance = getattr(stories, f"{selected_story}_story")
    text = story_instance.generate(user_input)

    return render_template('story.html', user_story=text)
