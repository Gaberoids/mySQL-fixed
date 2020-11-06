import os

import pymysql


# connect to the database
connection = pymysql.connect(host='localhost', 
                            db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of
    # whether the above was sucessful
    connection.close()

