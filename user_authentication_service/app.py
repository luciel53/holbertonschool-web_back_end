#!/usr/bin/env python3
"""
App file
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def payload():
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'])
def users():
    """
    implement the end-point to register a user. Define a users function
    that implements the POST /users route.
    """
    # get the data from the form
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # try to register
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        # if the user already exists
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
