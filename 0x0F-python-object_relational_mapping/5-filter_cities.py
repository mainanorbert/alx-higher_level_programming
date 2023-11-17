#!/usr/bin/python3
"""Lists all cities from the database"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    db_obj = db.cursor()
    db_obj.execute("SELECT cities.name FROM cities INNER JOIN \
            states ON states.id = cities.state_id WHERE states.name \
            LIKE BINARY %s ORDER BY cities.id ASC", (argv[4],))
    my_cities = db_obj.fetchall()
    city_list = ", ".join([city[0] for city in my_cities])
    print(city_list)
    db_obj.close()
    db.close()
