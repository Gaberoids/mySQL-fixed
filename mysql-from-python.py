# To test if connection is working video class
# import os #This is needed for cloud9 login
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                             db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM Artist;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

#-------------------------------------------#

# Cursor class
# import os
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         # pymysql.cursors.DictCursor will
#         # ...format return result (column name: value)
#         sql = "SELECT * FROM Artist;"
#         cursor.execute(sql)
#         # "for" will return the cursor in Json format. easier to read
#         for row in cursor:
#             print(row)
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Class create a table
# import os
# import datetime
# # because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                         Friends (name char(20), age int, DOB datetime);""")
#         result = cursor.fetchall()
#         print(result)
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Insert Rows video class
# import os
# import datetime
# # because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         row = ("Bob", 21, "1990-02-06 23:04:56")
#         cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# # -------------------------------------------#

# # Execute many inserts
# import os
# import datetime
# # because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         rows = [("Bob", 21, "1990-02-06 23:04:56"),
#                 ("Jim", 56, "1955-05-09 13:12:35"),
#                 ("Fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Update video class
# import os
# import datetime
# # because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()


# -------------------------------------------#

# Update video class
# import os
# import datetime
# # because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Alternate Update video class
# import os
# import datetime
# # because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", (23, 'Bob'))
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Update many video class
# import os
# import datetime
# # because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         rows = [(20, 'Bob'), (24, 'Jim'), (25, 'Fred')]
#         cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
#                             rows)
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Delete video class
# because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Alternate delete video class
# because table will have a cloumn datetime
# import pymysql
# # connect to the database
# connection = pymysql.connect(host='localhost',
#                              db='Chinook')
# try:
#     # Run a query for test
#     with connection.cursor() as cursor:
#         row = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
#         # because %s is being replace by one value we can just put 'bob'
#         connection.commit()
# finally:
#     # Close the connection, regardless of
#     # whether the above was sucessful
#     connection.close()

# -------------------------------------------#

# Delete many video class
# because table will have a cloumn datetime
import pymysql
# connect to the database
connection = pymysql.connect(host='localhost',
                             db='Chinook')
try:
    # Run a query for test
    with connection.cursor() as cursor:
        row = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ('bob','Jim', 'Fred'))
        connection.commit()
finally:
    # Close the connection, regardless of
    # whether the above was sucessful
    connection.close()
