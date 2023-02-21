"""
This file contain the details for the user login system.
"""
import requests
from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid


LIST = 'list'
DICT = 'dict'
DATA = "Data"
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'


URL = "https://project-finder.herokuapp.com/"
USERS_NS = 'users'
USER_DICT = f'/{DICT}'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_LIST = f'/{USERS_NS}/{LIST}'
USER_ADD = f'/{USERS_NS}/{ADD}'
USER_LOGIN = f'/{USERS_NS}/login'
USER_SIGNUP = f'/{USERS_NS}/signup'


def user_exists(users):
    response = requests.get(URL+USER_DETAILS+f'/{users}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def add_user(details):
    """
    send user to server
    """
    response = requests.post(URL+USER_ADD, json=details)
    if response.status_code == 200:
        return {MESSAGE: 'User added.'}
    else:
        print(f"Request failed with status code {response.status_code}")


def get_user_details(user):
    response = requests.get(URL+USER_DETAILS+f'/{user}')
    if response.status_code == 200:
        return response.json()['user detail']
    else:
        print(f"Request failed with status code {response.status_code}")


def user_login(details):
    response = requests.post(URL+USER_LOGIN, json=details)
    if response.status_code == 200:
        return {MESSAGE: 'User loged in.'}
    else:
        print(f"Request failed with status code {response.status_code}")


def user_signup(details):
    response = requests.post(URL+USER_LOGIN, json=details)
    if response.status_code == 200:
        return {MESSAGE: 'User created.'}
    else:
        print(f"Request failed with status code {response.status_code}")


class User:
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        """
        User registration
        """
        print(request.form)
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "phone": request.form.get('phone'),
            "password": request.form.get('password')
        }

        if user_exists(user['email']):
            return jsonify({"error": "Email address already existed"}), 400
        else:
            """Create a new user"""
            user_signup(user)

            """ Log the user in """
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400


    def signout(self):
        session.clear()
        return redirect('/')


    def login(self):

        """
        Create a dict for user input
        """
        user_field = {
            'email' : request.form.get('email'),
            'password' : request.form.get('password')
        }
        user_email = user_field['email']
        """
        Check if the user exist.
        """
        if user_exists(user_email):
            """ Log the user in """
            user_login(user_field)
            user = get_user_details(user_email)
            return self.start_session(user)

        else:
            return jsonify({"error": "Account not exists"}), 401

        return jsonify({"error": "Invalid login credentials"}), 401


def main():
    test_user = "yzzzz@nyu.edu"
    user_exists(test_user)

if __name__ == '__main__':
    main()