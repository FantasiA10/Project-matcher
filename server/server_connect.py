import requests

LIST = 'list'
DICT = 'dict'
DATA = "Data"
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'
CHANGE = 'change'
DELETE = 'delete'

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
