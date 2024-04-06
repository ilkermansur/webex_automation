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
import pprint

access_token = ""
               
header = {"Authorization" : "Bearer " + access_token}


def get_user_list():
    user_list = []
    url = "https://webexapis.com/v1/people"
    response = requests.get(url=url, headers=header)
    response = response.json()

    for i in range (len(response['items'])):
        user_dict = {}
        user_dict ['emails']= response['items'][i]['emails']
        user_dict ['id'] = response['items'][i]['id']
        user_dict ['displayName'] = response['items'][i]['displayName']
        if 'phoneNumbers' in  response["items"][i]: 
            user_dict ['phoneNumbers'] = response["items"][i]["phoneNumbers"][0]['value']
        user_list.append(user_dict)
    return user_list

def get_auto_atendant_list():
    auto_attendant_list = []
    url = "https://webexapis.com/v1/telephony/config/autoAttendants"
    response = requests.get(url=url, headers=header)
    response = response.json()
    for i in range (len(response['autoAttendants'])):
        auto_attendant_dict = {}
        auto_attendant_dict ['id'] = response['autoAttendants'][i]['id']
        auto_attendant_dict ['name'] = response['autoAttendants'][i]['name']
        auto_attendant_dict ['extension'] = response['autoAttendants'][i]['extension']
        auto_attendant_list.append(auto_attendant_dict)
    return auto_attendant_list

def get_hunt_group_list():
    hunt_group_list = []
    url = "https://webexapis.com/v1/telephony/config/huntGroups"
    response = requests.get(url=url, headers=header).json()
    return response

def update_hunt_group(locationId, huntGroupId, body_params):

    url = f"https://webexapis.com/v1/telephony/config/locations/{locationId}/huntGroups/{huntGroupId}"

    access_token = ""

    body_params = {
        "agents": [
            {"id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xYzhlYWViNy1jNTRlLTQ4MjUtOWM5ZS00MWRlYmU2NzE1NmU"},
            {"id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jOGY3M2UzNi02NmY0LTRkNzQtYjhjMS02ZDhmODI1Y2Q1MWQ"}     
            ]
    }
    header = {"Authorization" : "Bearer " + access_token}
    try:
        requests.put(url=url, headers=header, json=body_params)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

