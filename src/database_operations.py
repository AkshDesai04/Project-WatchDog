# import mysql.connector
import sqlite3


def create_db(name): #WorkedOn
    # mycursor = conn.cursor()
    # sql = f"CREATE DATABASE {name}"
    #
    # try:
    #     mycursor.execute(sql)
    #     conn.commit()
    #
    #     print("DataBase created successfully!")
    #
    # except mysql.connector.Error as err:
    #     print("Error:", err)
    #
    # mycursor.close()
    connection = sqlite3.connect(name)


def create_table(conn, name, fields, types, sizes, constraints): #ReadyToTest
    # mycursor = conn.cursor()
    #
    # #For Testing
    # # if len(fields) != len(types) or len(types) != len(sizes) or len(sizes) != len(constraints):
    #     # return "Input arrays must have the same length"
    # #For Testing
    #
    # descriptions = []
    # for i in range(len(fields)):
    #     desc = f"{fields[i]} {types[i]}({sizes[i]})"
    #     if constraints[i]:
    #         desc += " " + " ".join(constraints[i])
    #     descriptions.append(desc)
    # columns = ", ".join(descriptions)
    #
    # sql = f"CREATE TABLE {name} (" + columns + ")"
    # try:
    #     mycursor.execute(sql)
    #     conn.commit()
    #     print(sql)
    #
    #     print("Table created successfully!")
    #
    # except mysql.connector.Error as err:
    #     print("Error:", err)
    #
    # mycursor.close()
    curr = conn.cursor()
    curr.execute(f"drop table if exists {name}")

    query = f"create table {name} ("
    for i in range(0, fields.size()):
        query = f"\n{query} {fields[i]} {types[i]}({sizes[i]}) {constraints},"
    query = f"{query[:len(query) - 1]} );"

    print(query)
    conn.execute(query)

def create_conn(name): #ReadyToTest
    # conn = mysql.connector.connect(
    #     host      =  host,
    #     user      =  user,
    #     password  =  password,
    #     database = database
    # )
    # return conn
    conn = sqlite3.connect(name)
    return conn


def db_insert(table, *data): #ReadyToTest NoUpdatesMade Unsure
    curr = conn.cursor()
    
    _fields = []
    _datas = []

    for key, value in data.items():
        _fields.append(key)
        if isinstance(value, str):
            _datas.append(f"'{value}'")
        else:
            _datas.append(str(value))

    fields = ", ".join(_fields)
    datas = ", ".join(_datas)
    print(fields)
    print(datas)

    sql = f"insert into {table} ({fields}) values ({datas})"

    try:
        curr.execute(sql)
        conn.commit()
        print("sql: " + sql)
        print("fields: " + fields)
        print("datas: " + datas)
        
        print("Data inserted!")

    except mysql.connector.Error as err:
        print("Error:", err)

    curr.close()


def db_read(conn, query): #Work edOn
    curr = conn.cursor()
    curr.execute(query)
    return curr.fetchall()
    # try:
    #     curr = conn.cursor()
    #     curr.execute(query)
    #
    #     if cursor.with_rows:
    #         result = cursor.fetchall()
    #         if len(result) == 1 and len(result[0]) == 1:
    #             return result[0][0]
    #         else:
    #             return result
    #     else:
    #         return None
    # except Exception as e:
    #     return str(e)




def db_execute_cmd(conn, cmd): #Pending
    try:
        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False