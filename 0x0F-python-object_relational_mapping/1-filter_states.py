#!/usr/bin/python3
"""Listing states with name starting with N"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    db_obj = db.cursor()
    db_obj.execute("SELECT * FROM `states` ORDER BY `id`")
    for state in db_obj.fetchall():
        if (state[1][0] == "N"):
            print(state)

    db_obj.close()
    db.close()
