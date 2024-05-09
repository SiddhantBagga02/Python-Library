

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='sahil',database='db1')
cur=mydb.cursor()

# # creating database
cur.execute('create database db1')
#_______________________________________________________________________________________________________________________________
# # creating tables
s = 'create table student(name varchar(20),reg_no integer(8),cgpa float(3,2))'
cur.execute(s)
#_______________________________________________________________________________________________________________________________
# insering into tables
i = 'insert into student(name,reg_no,cgpa) values(%s,%s,%s)'
s1 = ("sahil",2211363,8.8)
cur.execute(i,s1)
mydb.commit()      
#_______________________________________________________________________________________________________________________________
# inserting many data into tables
i = 'insert into student(name,reg_no,cgpa) values(%s,%s,%s)'
s1 = [("shubham",2211346,7.5),("sid",2211280,7.5),("aleko",221180,7.8),("asnhit",2211696,8.0)]
cur.executemany(i,s1)
mydb.commit()
#_______________________________________________________________________________________________________________________________
# fetching data from table and printing
p = 'select * from student'
cur.execute(p)
result = cur.fetchall()
for rec in result:
    print(rec)
#_______________________________________________________________________________________________________________________________

# updating tables
u = 'UPDATE student SET cgpa=cgpa-1 where cgpa>=8'
cur.execute(u)
mydb.commit()
#_____________________________________________________________________________________________________________________________
# deleting table data
d = 'DELETE from student WHERE name ="sahil"'
cur.execute(d)
mydb.commit()
#_____________________________________________________________________________________________________________________________