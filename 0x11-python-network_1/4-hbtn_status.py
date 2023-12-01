#!/usr/bin/python3
"""Fetching from https://intranet.hbtn.io/status."""
from requests import get


if __name__ == "__main__":
    content = get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
