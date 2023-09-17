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
    cursor.execute("""SELECT id, name FROM states
                   ORDER BY states.id ASC;""")
    for record in cursor.fetchall():
        if record[1][0] == 'N':
            print(record)

