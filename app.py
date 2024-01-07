import json
import requests
import time

def perform_actions():
    with open('config.json', 'r') as file:
        data = json.load(file)

    auth_token = data.get('auth-token', None)

    if auth_token:
        api_url = 'https://api.bloxempire.com/hourly/get-hourly-info'
        headers = {'Authorization': auth_token}

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            response_json = response.json()
            is_joined = response_json.get('isJoined', None)

            if is_joined is not None and not is_joined:
                join_api_url = 'https://api.bloxempire.com/hourly/join-hourly'
                join_response = requests.post(join_api_url, headers=headers)

                if join_response.status_code == 200 and join_response.json().get('OK', False):
                    print("Successfully joined hourly giveaway")
                else:
                    print("Failed to join")
            else:
                print("Already Joined! Waiting 5 minutes..")
        else:
            print(f"Error: {response.status_code}")
    else:
        print("Auth token not found in the configuration.")

while True:
    perform_actions()
    time.sleep(300)
