#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    myurl = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(myurl) as response:
        content = response.read()
        my_cont = content.decode("utf-8")
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {my_cont}")
