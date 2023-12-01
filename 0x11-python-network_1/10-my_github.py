#!/usr/bin/python3
import requests
from sys import argv
"""
Python script that takes GitHub credentials
(username and personal access token)
and uses the GitHub API to display your user ID.
usage:
    ./10-my_github.py <user name> <personal access token>
"""


if __name__ == "__main__":
    # auth = requests.auth.HTTPBasicAuth(argv[1], argv[2]).json()
    res = requests.get("https://api.github.com/user",
                       auth=(argv[1], argv[2])).json()
    print(res.get("id"))
