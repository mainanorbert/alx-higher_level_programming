#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    my_data = f"email={argv[2]}".encode('utf-8')
    with urlopen(argv[1], my_data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
