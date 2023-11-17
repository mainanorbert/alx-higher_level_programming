#!/usr/bin/python3
# Python script tha lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py username <mysql> <password>  <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    db_obj = db.cursor()
    db_obj.execute("SELECT * FROM `states`")
    # [print(state) for state in db_obj.fetchall()]
    for state in db_obj.fetchall():
        print(state)
