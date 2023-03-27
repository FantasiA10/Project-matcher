import pymongo
import server.server_connect as sc
import requests
import datetime

"""
this file is used for checking currently available data.
"""

details = {
  "account": "string",
  "name": "string",
  "department_name": "string",
  "major_requirements": "string",
  "school_year": "string",
  "num_members": 0,
  "GPA": 0,
  "project_duration": "string",
  "skill requirements": "string",
  "description": "string",
  "post_date": "string",
  "if_approve": True
}
response = requests.post("https://project-finder.herokuapp.com/projects/add", json = details)
print(response.status_code)
response = requests.post("https://project-finder.herokuapp.com/projects/details/new project")
print(response.json())
#data = requests.get("https://project-finder.herokuapp.com/projects/dict")
#print(data.json())

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
    response = requests.get(URL+PROJECT_GET_FILE+f'/{name}'+'/1')
    filename = response.headers.get('content-disposition', '').split('"')[-2]
    file_mimetype, encoding  = mimetypes.guess_type(filename)
    return send_file(response.content,
                     as_attachment=True,
                     attachment_filename=filename,
                     mimetype=file_mimetype
                     )