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
    return render_template('index.html')
