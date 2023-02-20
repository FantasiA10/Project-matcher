"""
This module contains details about users.
"""
import db.db_connect as dbc

TEST_USER_EMAIL = 'Test'
NAME = 'name'
EMAIL = 'email'
PHONE = 'phone'
PW = 'password'

REQUIRED_FLDS = [EMAIL]

USER_KEY = 'email'
USER_COLLECT = 'users'


def get_users():
    dbc.connect_db()
    return dbc.fetch_all(USER_COLLECT)


def get_users_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(USER_KEY, USER_COLLECT)


def get_user_details(email):
    dbc.connect_db()
    return dbc.fetch_one(USER_COLLECT, {USER_KEY: email})


def user_exists(email):
    """
    check whether or not a user exists.
    """
    return get_user_details(email) is not None


def get_user_password(email):
    """
    return user registered passwrod in db
    """
    user = get_user_details(email)
    pw = user['password']
    return pw


def del_user(email):
    """
    Delete a doc from db collection by its name.
    """
    return dbc.del_one(USER_COLLECT, {USER_KEY: email})


def add_user(email, usr_details):
    dbc.connect_db()
    usr_details[USER_KEY] = email
    return dbc.insert_one(USER_COLLECT, usr_details)


def main():
    users = get_users()
    print(f'{users=}')
    print(f'{get_user_details(TEST_USER_EMAIL)=}')


if __name__ == '__main__':
    main()
