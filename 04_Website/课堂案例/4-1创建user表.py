import sqlite3
conn=sqlite3.connect('robot.db')
c=conn.cursor()
sql='''create table user(
        id integer primary key AUTOINCREMENT not null,
        username text,
        password text)'''
c.execute(sql)
conn.commit()
conn.close()