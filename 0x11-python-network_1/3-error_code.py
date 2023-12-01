#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the
response (decoded in utf-8).
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors."""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    myurl = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read.decode("ascii"))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))