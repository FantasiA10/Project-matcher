import requests
from flask import send_file

LIST = 'list'
DICT = 'dict'
DATA = "Data"
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'
CHANGE = 'change'
DELETE = 'delete'
VALUE = 'value'

TEST_PROJECT_NAME = 'Test project'
NAME = 'name'
ACCOUNT = 'account'
NUM_MEMBERS = 'num_members'
DEPARTMENT = 'department_name'
MAJOR = 'major_requirements'
SCHOOL_YEAR = 'school_year'
GPA = 'GPA'
LENGTH = 'project_duration'
SKILL = 'skill requirements'
POST_DATE = 'post_date'
DESCRIP = 'description'
APPROVE = "if_approve"
FIELD = 'field'
FILE = 'file'
DELETE = 'delete'

DATA_NS = 'data'
PROJECTS_NS = 'projects'
USERS_NS = 'users'

URL = "https://project-finder.herokuapp.com/"

PROJECT_KEY = 'name'
PROJECTS_COLLECT = 'projects'
PROJECT_DICT = f'/{PROJECTS_NS}/{DICT}'
PROJECT_LIST = f'/{PROJECTS_NS}/{LIST}'
PROJECT_ADD = f'/{PROJECTS_NS}/{ADD}'
PROJECT_DETAILS = f'/{PROJECTS_NS}/{DETAILS}'
PROJECT_CHANGE = f'/{PROJECTS_NS}/{CHANGE}'
PROJECT_FILE_DELETE = f'/{PROJECTS_NS}/{FILE}/{DELETE}'
PROJECT_FILE_ADD = f'/{PROJECTS_NS}/{FILE}/{ADD}'


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
    response = requests.post(URL+USER_SIGNUP, json=details)
    if response.status_code == 200:
        return {MESSAGE: 'User created.'}
    else:
        print(f"Request failed with status code {response.status_code}")


def get_project_details(project):
    response = requests.get(URL+PROJECT_DETAILS+f'/{project}')
    if response.status_code == 200:
        return response.json()['project detail']
    else:
        print(f"Request failed with status code {response.status_code}")


def get_projects_dict():
    response = requests.get(URL+PROJECT_DICT)
    if response.status_code == 200:
        project = response.json()
        return project[DATA]
    else:
        print(f"Request failed with status code {response.status_code}")


def del_project(name):
    """
    Delete a doc from db collection by its name.
    """
    


def del_one(name):
    """
    todo
    """


def exist(name):
    """
    todo
    """


def check_if_exist(project):
    """
    check whether or not a project exists.
    """
    response = requests.get(URL+PROJECT_DETAILS+f'/{project}')
    if response.status_code == 200:
        return response.json()['project detail']
    else:
        print(f"Request failed with status code {response.status_code}")


def add_project(details):
    """
    send project to server
    """
    response = requests.post(URL+PROJECT_ADD, json=details)
    if response.status_code == 200:
        return {MESSAGE: 'Project added.'}
    else:
        print(f"Request failed with status code {response.status_code}")


def change_project_single_field(name, field, val):
    """
    todo
    """
    request_dict = {NAME: name,
                    FIELD: field,
                    VALUE: val
                    }
    response = requests.post(URL+PROJECT_CHANGE, json=request_dict)
    if response.status_code == 200:
        return {MESSAGE: 'Project Changed.'}
    else:
        print(f"Request failed with status code {response.status_code}")


def add_file(file_detail):
    """
    add a description file to a project
    """
    name = file_detail['name']
    file_name = file_detail['filename']
    file_data = {'file': (file_name, file_detail['filedata'])}
    response_delete = requests.get(URL+PROJECT_FILE_DELETE)
    response_post = requests.post(URL+PROJECT_FILE_ADD + f'/{name}' +
                                  f'/{file_name}', files=file_data)
    if response_post.status_code == 200 and response_delete.status_code == 200:
        return {MESSAGE: 'Project Changed.'}
    else:
        print(f"Request failed with status code {response_post.status_code}")


def get_file_name(name):
    """
    get the name of the file
    """
    response = requests.get(URL+f'/{name}'+'/0')
    if response.status_code == 200:
        return response.json()['filename']
    return None


def get_file(name):
    """
    get the file for download
    """
    response = requests.get(URL+f'/{name}'+'/1')
    return send_file(response,
                     as_attachment=True,
                     attachment_filename=response.filename)
