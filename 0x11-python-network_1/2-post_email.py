#!/usr/bin/python3
import urllib.request
import urllib.parse
from sys import argv
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of theresponse (decoded in utf-8)"""


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    with urllib.request.urlopen(argv[1], data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
