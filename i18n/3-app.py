#!/usr/bin/env python3
"""
Flask App file
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    Then instantiate the Babel object in your app. Store it in a
    module-level variable named babel.
    In order to configure available languages in our app, you will create
    a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
    Use Config to set Babel’s default locale ("en") and timezone ("UTC").

    Use that class as config for your Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('3-app.Config')


@babel.localeselector
def get_locale():
    """ function determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=['GET'])
def index():
    """ Return the index page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
