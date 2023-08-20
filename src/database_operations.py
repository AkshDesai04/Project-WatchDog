import mysql.connector

def create_db(connection, name):    #Done
    mycursor = connection.cursor()
    sql = f"CREATE DATABASE {name}"

    try:
        mycursor.execute(sql)
        connection.commit()

        print("DataBase created successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)

    mycursor.close()
    connection.close()


def create_table(con, name, fields, type, size):
    #fields, type, and size are arrays
    pass


def create_connection(host, user, password, database):
    mydb = mysql.connector.connect(
        host      =  host,
        user      =  user,
        password  =  password,
        database  =  database
    )
    return mydb


def db_insert(con, table, *data):
    mycursor = con.cursor()

    _data = ""
    for i in data:
        _data + ", " + i
    _data = _data[:-2]

    sql = f"INSERT INTO customers VALUES ({_data})"
    mycursor.execute(sql)
    con.commit()


def db_read(con, query):
    mycursor = con.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    return mycursor


def db_execute_cmd(con, quercmd):
    mycursor = con.cursor()
    mycursor.execute(cmd)