#!/usr/bin/python3
import os
import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv[1:]
    cursor = MySQLdb.connect(host="localhost", user=args[0], password=args[1], database=args[2], port=3306).cursor()

    cursor.execute("SELECT id, name FROM states;")
    for record in cursor.fetchall():
        print(record)