#!/usr/bin/env python3
"""
Flask App file
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=['GET'])
def index():
    """ Return the index page """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000",debug=True)
