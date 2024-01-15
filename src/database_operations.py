# import mysql.connector
import sqlite3

def create_db(name): #Works
    connection = sqlite3.connect(name)


def create_table(conn, name, fields, types, sizes, constraints): #Works
    curr = conn.cursor()
    curr.execute(f"drop table if exists {name}")

    query = f"create table {name} ("
    for i in range(0, len(fields)):
        query = f"\n{query} {fields[i]} {types[i]}({sizes[i]}) {constraints[i]},"
    query = f"{query[:len(query) - 1]} );"

    print(query)
    conn.execute(query)

def create_conn(name): #Works
    conn = sqlite3.connect(name)
    return conn


def db_insert(conn, table, data): #Works
    curr = conn.cursor()

    _data = ""

    for i in range(len(data)):
        _data = _data + ("\'" if type(_data) is str else "") + str(data[i]) + ("\'" if type(_data) is str else "") + ", "
    _data = _data[:len(_data) - 2]

    sql = f"insert into {table} values ({_data});"

    try:
        curr.execute(sql)
        conn.commit()
    except Exception as err:
        print("Error: ", err)


def db_read(conn, query): #ReadyToTest
    curr = conn.cursor()
    curr.execute(query)
    return curr.fetchall()


def db_execute_cmd(conn, cmd): #Works
    try:
        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False