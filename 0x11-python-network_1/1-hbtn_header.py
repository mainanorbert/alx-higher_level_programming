#!/usr/bin/python3
"""Python script that takes in a URL, sends 
a request to the URL and displays the value of the X-Request-Id variable found in the header
of the response."""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_req_id = response.headers["X-Request-Id"]
        print(x_req_id)

