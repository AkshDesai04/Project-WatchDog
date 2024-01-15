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


def db_read(conn, query): #ReadyToTest
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




def db_execute_cmd(conn, cmd): #ReadyToTest #Unsure #LessChangesMade
    try:
        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False




































#Testing Playground

# create_db('test_db.db')
# create_table(create_conn('test_db.db'), 'TestTable', ['id', 'name', 'number'], ['number', 'varchar2', 'number'], [3, 30, 10], ['primary key', 'not null', 'unique'])
print(create_conn('test_db.db'))

#Testing Playground