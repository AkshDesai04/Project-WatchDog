import mysql.connector

def create_db(conn, name):    #Done
    mycursor = conn.cursor()
    sql = f"CREATE DATABASE {name}"

    try:
        mycursor.execute(sql)
        conn.commit()

        print("DataBase created successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)

    mycursor.close()


def create_table(conn, name, fields, types, sizes, constraints): #Done
    mycursor = conn.cursor()

    #For Testing
    # if len(fields) != len(types) or len(types) != len(sizes) or len(sizes) != len(constraints):
        # return "Input arrays must have the same length"
    #For Testing

    descriptions = []
    for i in range(len(fields)):
        desc = f"{fields[i]} {types[i]}({sizes[i]})"
        if constraints[i]:
            desc += " " + " ".join(constraints[i])
        descriptions.append(desc)
    columns = ", ".join(descriptions)

    sql = f"CREATE TABLE {name} (" + columns + ")"
    try:
        mycursor.execute(sql)
        conn.commit()
        print(sql)
        
        print("Table created successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)

    mycursor.close()


def create_conn(host, user, password, database):
    mydb = mysql.connector.connect(
        host      =  host,
        user      =  user,
        password  =  password,
        database  =  database
    )
    return mydb


def db_insert(conn, table, *data): #Done
    mycursor = conn.cursor()
    
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
        mycursor.execute(sql)
        conn.commit()
        print("sql: " + sql)
        print("fields: " + fields)
        print("datas: " + datas)
        
        print("Data inserted!")

    except mysql.connector.Error as err:
        print("Error:", err)

    mycursor.close()


def db_read(conn, query): #Done
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        
        if cursor.with_rows:
            result = cursor.fetchall()
            if len(result) == 1 and len(result[0]) == 1:
                return result[0][0]
            else:
                return result
        else:
            return None
    except Exception as e:
        return str(e)


def db_execute_cmd(conn, cmd): #Done
    try:
        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False