#!/usr/bin/python3
"""script that takes argument and
displays states matching argument"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    db_obj = db.cursor()
    db_obj.execute("SELECT * FROM `states` WHERE BINARY `name` = '{}' ORDER BY id ASC".format(argv[4]))
    for state in db_obj.fetchall():
            print(state)
    db_obj.close()
    db.close()
