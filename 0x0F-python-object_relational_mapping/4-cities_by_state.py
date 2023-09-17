#!/usr/bin/python3
''' Module demonstrating the use of the MySQLdb database API '''
import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", user=args[0], password=args[1],
                         database=args[2], port=3306)
    cursor = db.cursor()
    assert type(cursor) is MySQLdb.cursors.Cursor
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC;""")
    for record in cursor.fetchall():
        print(record)
