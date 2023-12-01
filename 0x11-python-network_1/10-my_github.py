#!/usr/bin/python3
"""
Python script that takes GitHub credentials
(username and personal access token)
and uses the GitHub API to display your user ID.
usage:
    ./10-my_github.py <user name> <personal access token>
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
