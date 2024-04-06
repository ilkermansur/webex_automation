"""
This Python script is written for a specific purpose and reflects its current state. However, no warranty is provided. 
Usage of this script is entirely at the user's own risk. The developer  or  contributors cannot be held liable for any 
direct or indirect damages that may arise from the use or misuse of this script.

Developer: ilker MANSUR
Email: imansur@morten.com.tr
GitHub: github.com/ilkermansur

get_user_list() function returns the list of users in the Webex organization.
get_auto_atendant_list() function returns the list of auto attendants in the Webex organization.

"""

import requests
import json
import re

begin_date = "2024-03-01" # Format 1970-01-01
end_date = "2024-03-30" 

url = f"https://webexapis.com/v1/recordings?from={begin_date}T01:00:00.000Z&to={end_date}T23:59:00.000Z&max=100"


access_token = "MWVjOWJiMjktYTlkMS00ZTBhLWFjNzktZDNmNjRmYjJmZjM1ZDM0ZDM3MWItM2Q1_PF84_9e0f5026-c7df-4241-8b3a-c2d4fe59e5d0"

header = {"Authorization" : "Bearer " + access_token}
response = requests.get(url=url, headers=header)
resp = response.json()['items']

for record in resp:
    print (' Recording Room     : '+ record['topic'])
    print (' Download URL       : '+ record['downloadUrl'])
    print (' Download  Password : '+ record['password'])
    print (100*'-')


