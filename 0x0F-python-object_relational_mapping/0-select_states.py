#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve all the states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows and store them in a variable
    rows = cursor.fetchall()

    # Loop through the rows and print out the state information
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
