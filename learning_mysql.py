import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="sahil",database='shubham')
cur = mydb.cursor()

# a = "create database shubham"
# cur.execute(a)

# b = 'create table hostel_info(name varchar(20),age int(2),reg_no int(3),cgpa float(2,1))'
# cur.execute(b)

# # inserting into tables
# c = 'insert into hostel_info(name,age,reg_no,cgpa) values(%s,%s,%s,%s)'
# s1 = ("sahil",20,363,8)
# cur.execute(c,s1)
# mydb.commit()

# # inserting many into tables
# c = 'insert into hostel_info(name,age,reg_no,cgpa) values(%s,%s,%s,%s)'
# s1 = [("siddhnat",15,280,2),("shubham",26,346,1)]
# cur.executemany(c,s1)
# mydb.commit()

# fetch from tables
# e = 'select * from hostel_info'
# cur.execute(e)
# result = cur.fetchall()
# for item in result:
#     print(item)