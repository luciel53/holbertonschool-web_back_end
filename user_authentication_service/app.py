#!/usr/bin/env python3
"""
App file
"""
from os import getenv
from flask import Flask, jsonify, abort, request, redirect
from sqlalchemy.orm.exc import NoResultFound
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


@app.route('/sessions', methods=['POST'])
def login():
    """
    login function to respond to the POST /sessions route.

The request is expected to contain form data with "email" and a "password"
fields.

If the login information is incorrect, use flask.abort to respond with a
401 HTTP status.

Otherwise, create a new session for the user, store it the session ID as a
cookie with key "session_id" on the response and return a JSON payload of
the form
    """
    # get email and password
    email = request.form.get('email')
    password = request.form.get('password')

    # check login informations
    if AUTH.valid_login(email, password):
        # create session for user and generate a new id
        session_id = AUTH.create_session(email=email)
        response = jsonify({"email": email, "message": "logged in"})
        # store session id inasmuch as cookie
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/session', methods=['DELETE'])
def logout():
    """
    logout function to respond to the DELETE /sessions route.
    The request is expected to contain the session ID as a cookie with key
    "session_id".

    Find the user with the requested session ID. If the user exists destroy
    the session and redirect the user to GET /. If the user does not exist,
    respond with a 403 HTTP status.
    """
    # get the sessionID as cookie with request
    session_id_cookie = request.cookies.get('session_id')

    try:
        # Find the user with the requested session ID
        find_user = AUTH.get_user_from_session_id(session_id_cookie)
        # if the user exists, destroy session and redirect to GET /
        if find_user:
            AUTH.destroy_session(find_user.id)
            return redirect('/', code=302)
    except NoResultFound:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
