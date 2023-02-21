import pymongo
import db.projects as pj
import server.server_connect as sc
import requests
import datetime
import db.db_connect as connect

"""
this file is used for checking currently available data.
"""

def curr_data():
    client = pymongo.MongoClient('mongodb+srv://tracyzhu0608:1234@cluster0.8pa03kh.mongodb.net/?retryWrites=true&w=majority', 27017)
    db1 = client.projectdb
    
    result = db1.list_collection_names(session = None)
    print("forms in projectdb:", result)
    for ele in result:
        var = db1[ele].find()
        print(ele, " table")
        for doc in var:
            print(doc)

    db2 = client.user_login_system
    result = db2.list_collection_names(session = None)
    print("forms in user_login_system:", result)
    print("users table")
    var = db2.users.find()
    for doc in var:
        print(doc)
    print(pj.get_projects_dict())

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
#data = requests.get("https://project-finder.herokuapp.com/projects/dict")
#print(data.json())