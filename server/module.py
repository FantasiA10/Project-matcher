import heapq
import datetime
import server.server_connect as sc
from functools import wraps
import difflib
from flask import session, redirect


#export data from database
#todo give top matches
def homepage_form(key_word=None, approve=True):
    """
    Return project list
    """
    temp_project_dict = sc.get_projects_dict()
    project_lst = []
    project_dict = {}
    for key in temp_project_dict:
    #todo add time limit functions like (datetime.datetime.today() 
    # - temp_project_dict[key]['post_date']).days < 90
        if approve:
            if temp_project_dict[key]['if_approve']:
                project_lst.append(temp_project_dict[key])
                project_dict[key] = temp_project_dict[key]
        else:
            if not temp_project_dict[key]['if_approve']:
                project_lst.append(temp_project_dict[key])
                project_dict[key] = temp_project_dict[key]
    
    if not key_word or not temp_project_dict:
        return project_lst
    return rank_for_relation_to_key_work(project_dict, key_word.lower())


def dict_to_lst_of_string(project_dict):
    """
    transfer dict to list store with content as plain text and keys
    """
    ret_lst = []
    for key in project_dict:
        temp = ''
        for sub_key in project_dict[key]:
            if sub_key == 'account':
                temp = temp + project_dict[key]["account"]['email'] + " " + \
                    project_dict[key]["account"]['name']
            elif isinstance(project_dict[key][sub_key], str):
                temp += " " + project_dict[key][sub_key]
        ret_lst.append([key, temp.lower()])
    return ret_lst


def rank_for_relation_to_key_work(project_dict, key_word):
    """
    return ranked project based on relation to key_word
    """
    unrank_lst = dict_to_lst_of_string(project_dict)
    heap = []
    ret_project_lst = []
    for ele in unrank_lst:
        score = difflib.SequenceMatcher(None, key_word, ele[1]).ratio()
        heapq.heappush(heap, (-score, ele[0]))
    while len(heap) > 0:
        curr_proj = project_dict[heapq.heappop(heap)[1]]
        ret_project_lst.append(curr_proj)
    return ret_project_lst


# Decorators
def login_required(f):
    """
    Decorators
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap


def application_form(key_word=None):
    """
    Return application list
    """
    temp_application_dict = sc.get_applications_dict()
    application_lst = []
    application_dict = {}
    for key in temp_application_dict:
        application_lst.append(temp_application_dict[key])
        application_dict[key] = temp_application_dict[key]
    
    if not key_word or not temp_application_dict:
        return application_lst
    return rank_for_relation_to_key_work(application_dict, key_word.lower())


def dict_to_lst_of_string(application_dict):
    """
    transfer dict to list store with content as plain text and keys
    """
    ret_lst = []
    for key in application_dict:
        temp = ''
        for sub_key in application_dict[key]:
            if sub_key == 'account':
                temp = temp + application_dict[key]["account"]['email'] + " " + \
                    application_dict[key]["account"]['name']
            elif isinstance(application_dict[key][sub_key], str):
                temp += " " + application_dict[key][sub_key]
        ret_lst.append([key, temp.lower()])
    return ret_lst


def rank_for_relation_to_key_work(application_dict, key_word):
    """
    return ranked application based on relation to key_word
    """
    unrank_lst = dict_to_lst_of_string(application_dict)
    heap = []
    ret_application_lst = []
    for ele in unrank_lst:
        score = difflib.SequenceMatcher(None, key_word, ele[1]).ratio()
        heapq.heappush(heap, (-score, ele[0]))
    while len(heap) > 0:
        curr_proj = application_dict[heapq.heappop(heap)[1]]
        ret_application_lst.append(curr_proj)
    return ret_application_lst
