import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="root")
cur = con.cursor()

# database_operations.create_db(con, "ProjectWatchDog")
cur.execute("create database ProjectWatchDog")
con.database = "ProjectWatchDog"

con.close()