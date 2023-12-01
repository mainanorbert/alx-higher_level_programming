#!/usr/bin/python3
import requests
import sys
"""
Python script that takes GitHub credentials
(username and personal access token)
and uses the GitHub API to display your user ID.
usage: ./10-my_github.py <user name> <personal access token>
"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
        sys.exit(1)
    username = sys.argv[1]
    token = sys.argv[2]
    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'Basic {username}:{token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id', 'User ID not found')
        print(f"{user_id}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
