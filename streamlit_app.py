import cx_Oracle

connection = cx_Oracle.connect(
    user="demopython",
    password="XXXXX",
    dsn="localhost/xepdb1")

sl.write("Successfully connected to Oracle Database")
