import sqlite3

conn = sqlite3.connect('Test_DB.db') #making or connecting to existing database
curs = conn.cursor()
# curs.execute('drop table if exists test_table')
# curs.execute('create table test_table(id number(5) primary key, name varchar2(20));')
# curs.execute("insert into test_table(id, name) values(5, 'Aksh');")
curs.execute('select * from test_table;')
# curs.execute('commit;')
print(curs.fetchall())