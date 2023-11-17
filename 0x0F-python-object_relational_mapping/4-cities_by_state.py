#!/usr/bin/python3
"""Lists all cities from the database"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    db_obj = db.cursor()
    db_obj.execute("SELECT cities.id, cities.name, states.name FROM `cities` \
            INNER JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    for city in db_obj.fetchall():
        print(city)
    db_obj.close()
    db.close()
