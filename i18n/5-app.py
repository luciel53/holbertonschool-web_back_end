#!/usr/bin/env python3
"""
Flask App file
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
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
def get_locale() -> str:
    """ function determine the best match with our supported languages """
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=['GET'])
def index():
    """ Return the index page """
    return render_template('5-index.html')


def get_user():
    """ returns user dict """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
        else:
            return None


@app.before_request
def before_request():
    """ before request function """
    g.user = get_user()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
