import requests

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

LIST = 'list'
DICT = 'dict'
DATA = "Data"
HELLO = '/hello'
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'
CHANGE = 'change'
DELETE = 'delete'

PROJECT_KEY = 'name'
PROJECTS_COLLECT = 'projects'
DATA_NS = 'data'
PROJECTS_NS = 'projects'
USERS_NS = 'users'
SPONSORS_NS = 'sponsors'

JASON_TYPE = 'json'
STR_TYPE = 'str'

URL = "https://project-finder.herokuapp.com/"
PROJECT_DICT = f'/{PROJECTS_NS}/{DICT}'
PROJECT_LIST = f'/{PROJECTS_NS}/{LIST}'
PROJECT_ADD = f'/{PROJECTS_NS}/{ADD}'
PROJECT_DETAILS = f'/{PROJECTS_NS}/{DETAILS}'

def get_project_details(project):
    response = requests.post(URL+PROJECT_DETAILS+f'/{project}')
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
    return dbc.del_one(PROJECTS_COLLECT, {PROJECT_KEY: name})


def del_one(name):
    del projects[name]


def exist(name):
    return name in projects


def check_if_exist(name):
    """
    check whether or not a project exists.
    """
    response = requests.post(URL+PROJECT_DETAILS+f'/{name}')
    if response.status_code == 200:
        return {MESSAGE: 'Project added.'}
    else:
        print(f"Request failed with status code {response.status_code}")
    return get_project_details(name) is not None


def add_project(details):
    response = requests.post(URL+PROJECT_ADD, JSON_TYPE = details)
    if response.status_code == 200:
        return {MESSAGE: 'Project added.'}
    else:
        print(f"Request failed with status code {response.status_code}")


def change_project_single_field(name, field, val):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')

    if not isinstance(field, str):
        raise TypeError(f'Wrong type for details: {type(field)=}')
    dbc.connect_db()
    return dbc.change_one(NAME, name, APPROVE, val, PROJECTS_COLLECT)