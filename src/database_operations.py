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


def db_read(conn, query):
    mycursor = con.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    return mycursor


def db_execute_cmd(conn, quercmd):
    mycursor = con.cursor()
    mycursor.execute(cmd)