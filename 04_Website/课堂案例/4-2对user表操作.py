import sqlite3
#读取网站的所有用户名和密码
conn=sqlite3.connect('robot.db')
c=conn.cursor()   #获取游标
#在数据表user插入一行记录
c.execute("insert into user(username,password) values ('alice','12345')")
c.execute("insert into user(username,password) values('%s','%s')"%('jack','112233'))
#更新数据库
conn.commit()
#关闭数据库
conn.close()