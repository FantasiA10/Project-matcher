"""
This file contain the details for the user login system.
"""
import requests
from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid

import server.server_connect as sc


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

        if sc.user_exists(user['email']):
            return jsonify({"error": "Email address already existed"}), 400
        else:
            """Create a new user"""
            sc.user_signup(user)

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
        if sc.user_exists(user_email):
            """ Log the user in """
            if sc.user_login(user_field) == 200:
                sc.user_login(user_field)
                user = sc.get_user_details(user_email)
                return self.start_session(user)
            else:
                return jsonify({"error": "Invalid login credentials"}), 401
        else:
            return jsonify({"error": "Account not exists"}), 401

        return jsonify({"error": "Invalid login credentials"}), 401


def main():
    test_user = "yzzzz@nyu.edu"
    sc.user_exists(test_user)

if __name__ == '__main__':
    main()