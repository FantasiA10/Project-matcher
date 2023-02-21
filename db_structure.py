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