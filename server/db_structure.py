import pymongo
import server.server_connect as sc
import requests
import datetime

"""
this file is used for checking currently available data.
"""

apl_details = {
            'application_name': "1",
            'applicant_name': "1",
            'applicant_email': "1",
            'applied_project': "1",
            'application_date': "1",
            'application_status': "Pending",
            'resume_filename': resume_file.filename if resume_file else None,
            'resume_content': resume_file.read() if resume_file else None,
            'transcript_filename': transcript_file.filename if transcript_file else None,
            'transcript_content': transcript_file.read() if transcript_file else None,
            'coverletter_filename': coverletter_file.filename if coverletter_file else None,
            'coverletter_content': coverletter_file.read() if coverletter_file else None,
        }