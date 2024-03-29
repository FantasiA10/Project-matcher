import requests
from flask import send_file
import mimetypes
import io
import base64
import os

LIST = 'list'
DICT = 'dict'
DATA = "Data"
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'
CHANGE = 'change'
DELETE = 'delete'
VALUE = 'value'
USER = 'user'

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
GET = 'get'

PROJECTS_NS = 'projects'
USERS_NS = 'users'
APPLICATIONS_NS = 'application'
APPLICANT_NAME = 'applicant_name'
APPLICANT_EMAIL = 'applicant_email'
PROJECT = 'project'
APP_DATE = 'application_date'
RESUME = 'resume'
TRANSCRIPT = 'transcript'
STAT = 'statistic'
DEPART = 'departments'
PROFILE = 'profile'
UPDATE = 'update'

URL = os.environ.get('URL')
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
PROJECT_GET_FILE = f'/{PROJECTS_NS}/{FILE}/{GET}'
PROJECT_USER = f'/{PROJECTS_NS}/{USER}'
PROJECT_DELETE = f'/{PROJECTS_NS}/{DELETE}'
PROJECT_STATISTIC = f'/{PROJECTS_NS}/{STAT}'
PROJECT_DEPART = f'/{PROJECTS_NS}/{DEPART}'

USER_DICT = f'/{DICT}'
USER_DETAILS = f'/{USERS_NS}/{DETAILS}'
USER_LIST = f'/{USERS_NS}/{LIST}'
USER_ADD = f'/{USERS_NS}/{ADD}'
USER_LOGIN = f'/{USERS_NS}/login'
USER_SIGNUP = f'/{USERS_NS}/signup'
USER_UPDATE_PROFILE_PIC = f'/{USERS_NS}/{PROFILE}/{UPDATE}'
USER_GET_PROFILE_PIC = f'/{USERS_NS}/{PROFILE}/{GET}'
USER_DELETE = f'/{USERS_NS}/{DELETE}'
USER_UPDATE = f'/{USERS_NS}/{UPDATE}'

APPLICATION_DICT = f'/{APPLICATIONS_NS}/{DICT}'
APPLICATION_DETAILS = f'/{APPLICATIONS_NS}/{DETAILS}'
APPLICATION_LIST = f'/{APPLICATIONS_NS}/{LIST}'
APPLICATION_ADD = f'/{APPLICATIONS_NS}/{ADD}'
APPLICATION_USER = f'/{APPLICATIONS_NS}/{USER}'
APPLICATION_PROJECT = f'/{APPLICATIONS_NS}/{PROJECT}'
APPLICATION_DELETE = f'/{APPLICATIONS_NS}/{DELETE}'

"""
USER ENPOINTS
"""
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
    return response.status_code


def user_signup(details):
    response = requests.post(URL+USER_SIGNUP, json=details)
    if response.status_code == 200:
        return {MESSAGE: 'User created.'}
    else:
        print(f"Request failed with status code {response.status_code}")


def delete_user(user_email):
    """
    Delete an account in db
    """
    response = requests.post(URL+USER_DELETE+f'/{user_email}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def update_user(details):
    """
    Update an account
    """
    response = requests.post(URL+USER_UPDATE, json=details)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


""" 
PROJECTS 
"""

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


def get_projects_names():
    """
    Return a list of project names. This is used for the dropdown memu in the application form.
    """
    response = requests.get(URL+PROJECT_LIST)
    if response.status_code == 200:
        return response.json()["projects_list"]
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


def project_exist(project):
    """
    check whether or not a project exists.
    """
    response = requests.get(URL+PROJECT_DETAILS+f'/{project}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def add_project(details):
    """
    send project to server
    """
    response = requests.post(URL+PROJECT_ADD, json=details)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def get_statistic_dict():
    """
    get statistic result about web from server
    """
    response = requests.get(URL+PROJECT_STATISTIC)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def delete_project(project_name):
    """
    Allow users to delete their projects
    """
    response = requests.post(URL+PROJECT_DELETE+f'/{project_name}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def get_user_project(user_email):
    """
    Get all projects of a user
    """
    response = requests.get(URL+PROJECT_USER+f'/{user_email}')
    if response.status_code == 200:
        return response.json()
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
    response = requests.get(URL+PROJECT_GET_FILE+f'/{name}'+'/0')
    if response.status_code == 200:
        the_dict = response.json()
        """ 
        Check if the project has uploaded file
        """
        if 'filename' in the_dict:
            return response.json()['filename']
        return None
    return None


def get_file(name):
    """
    get the file for download
    """
    response_check = requests.get(URL+PROJECT_GET_FILE+f'/{name}'+'/0')
    if "filename" in response_check.json():
        response = requests.get(URL+PROJECT_GET_FILE+f'/{name}'+'/1')
        filename = response.headers.get('content-disposition', '').split('=')[-1]
        file_mimetype, encoding  = mimetypes.guess_type(filename)
        file_data = io.BytesIO(response.content)
        return send_file(file_data,
                         as_attachment=True,
                         attachment_filename=filename,
                         mimetype=file_mimetype
                         )
    else:
        return None


def update_profile_pic(profile_detail):
    """
    update a person profile picture
    """
    email = profile_detail['user_email']
    file_name = profile_detail['filename']
    file_data = {'file': (file_name, profile_detail['filedata'])}
    response_post = requests.post(URL + USER_UPDATE_PROFILE_PIC + f'/{email}' +
                                  f'/{file_name}', files=file_data)
    if response_post.status_code == 200:
        return {MESSAGE: 'Profile Picture Changed.'}
    else:
        print(f"Request failed with status code {response_post.status_code}")


def get_profile_pic(email):
    """
    get user picture from server
    """
    response = requests.get(URL+USER_GET_PROFILE_PIC+f'/{email}')
    if response.status_code == 200:
        if 'application/json' not in response.headers.get('Content-Type'):
            filename = response.headers.get('content-disposition', '').split('=')[-1]
            file_mimetype, encoding  = mimetypes.guess_type(filename)
            file_data = base64.b64encode(response.content).decode('utf-8')
            return file_mimetype, file_data
    return None, None


"""
Application
"""


def get_application_details(application):
    response = requests.get(URL+APPLICATION_DETAILS+f'/{application}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def get_applications_dict():
    response = requests.get(URL+APPLICATION_DICT)
    if response.status_code == 200:
        application = response.json()
        return application[DATA]
    else:
        print(f"Request failed with status code {response.status_code}")


def application_exist(application):
    """
    check whether or not an application exists.
    """
    response = requests.get(URL+APPLICATION_DETAILS+f'/{application}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def get_user_application(user_email):
    """
    Get all applications of a user
    """
    response = requests.get(URL+APPLICATION_USER+f'/{user_email}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")

    
def get_project_application(project):
    """
    Get all applications of a project
    """
    response = requests.get(URL+APPLICATION_PROJECT+f'/{project}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def get_project_application_file(project, applicant_email, field):
    """
    get application resume, coverletter, transcript based on request
    """
    response = requests.get(URL+APPLICATION_PROJECT+f'/{project}')
    if response.status_code == 200:
        application_lst = response.json()[project]
        for sub_dict in application_lst:
            if sub_dict['applicant_email'] == applicant_email:
                if field == 'resume':
                    file_mimetype, encoding  = mimetypes.guess_type('resume_filename')
                    file_data = io.BytesIO(sub_dict['resume_content'].encode())
                    return send_file(file_data,
                                     as_attachment=True,
                                     attachment_filename=sub_dict['resume_filename'],
                                     mimetype=file_mimetype
                                     )
                elif field == 'transcript':
                    file_mimetype, encoding  = mimetypes.guess_type('transcript_filename')
                    file_data = io.BytesIO(sub_dict['transcript_content'].encode())
                    return send_file(file_data,
                                     as_attachment=True,
                                     attachment_filename=sub_dict['transcript_filename'],
                                     mimetype=file_mimetype
                                     )
                elif field == 'coverletter':
                    file_mimetype, encoding  = mimetypes.guess_type('coverletter_filename')
                    file_data = io.BytesIO(sub_dict['coverletter_content'].encode())
                    return send_file(file_data,
                                     as_attachment=True,
                                     attachment_filename=sub_dict['coverletter_filename'],
                                     mimetype=file_mimetype
                                     )
    return None

        


def add_application(details):
    """
    send application to server
    """
    print(details)
    response = requests.post(URL+APPLICATION_ADD, json=details)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def delete_application(application_name):
    """
    Allow users to withdraw their applications
    """
    response = requests.post(URL+APPLICATION_DELETE+f'/{application_name}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


def get_departments():
    """
    Return a list of departments. This is used for the dropdown memu in the add project form.
    """
    response = requests.get(URL+PROJECT_DEPART)
    if response.status_code == 200:
        return response.json()["departments"]
    else:
        print(f"Request failed with status code {response.status_code}")
