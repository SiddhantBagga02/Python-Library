# i=1
# j=3
# for item in range(1,3):
#     print("*"*i)
#     i+=1

# for items in range(4,1,-1):
#     print("*"*j)
#     j-=1


# print the pattern *
# **
# ***
# **
# *

# define the number of rows


# print the upper half of the pattern
# i = 1
# for item in range(1, 4):
#     # print i stars
#     print("*" * i)
#     i = i + 1

# # print the lower half of the pattern
# j = 3
# for items in range(j, 1,-1):
#     # print j stars
#     print("*" * j)
    # j = j - 1





# # define the number of rows
# rows = 4

# # print the upper half of the pattern
# for i in range(1, rows + 1):
#     # print the digits from 1 to i
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# # print the lower half of the pattern
# for i in range(rows - 1, 0, -1):
#     # print the digits from 1 to i
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# a = "sahil is my first name"
# b = "mall"
# print(a.split())
# print(a.upper())
# print(b.isupper())


# a={1:"sahil",2:"shubham",3:"siddhant"}
# # print(a[1])
# # a[3]="sahaj"
# # print(a)
# # a[4]="siddhant"
# # print(a)
# # del(a[1])
# # print(a)
# for k in a.keys():
#     print(f"{k} is corresponding to {a[k]}")


# try:
#     a = int(input("entre a number: "))
#     b = int(input("entre another number: "))
#     c=a*b
#     print(c)
# except:
#     print("please entre a valid integer")
# finally:
#     print("rest of prgramme")










# a = [1,2,3,4]
# -----------------------------------------------
# map function
# def f(x):
#     d=(x*x)
#     return d
# b = map(f,a)
# print(list(b))
# -----------------------------------------------
# filtre function
# def fil(x):
#     if (x%2 == 0):
#         return x
# c = filter(fil,a)
# print(list(c))
# ----------------------------------------------
# reduce function
# from functools import reduce
# def plus1(x,y):
#     return(x+y)
# d = reduce(plus1,a)
# print(d)

    
# #function inside function 
# def sum_of_square(x,y):
#     def square(z):
#         return z*z
#     return(square(x)+square(y))

# # function as para meter
# def f(z):
#     return z*z
# def a(f,x):
#     return f(x)

# function returning function
# def outer_function():
#     print("outer function")
#     def inner_function():
#         print("inner function")
#     return inner_function
# c = outer_function()
# print(c)

# classes in python
# class circle:
#     def cal_area(self,r):
#         area1 = 3.14*(r**2)
#         return area1
    
# c = circle()
# print(c.cal_area(3))

# class employee:
#     def __init__(self,first,secound,age):
#         self.first_name = first
#         self.secound_name = secound
#         self.age = age
#     def full_name(self):
#         print(f"{self.first_name} {self.secound_name}")
# a = employee("sahil","mall",20)
# print(a.full_name())
# b = employee("subham","mallu",40)
# c = 0
# print(b.full_name())
# #use of isinstance()method
# print(isinstance(b,employee))
# print(isinstance(c,employee))


# class self_demu:
#     def methoda(self):
#         print("method a is called")
#     def methodb(self):
#         print("method a called method b ")
#         self.methoda()
# a = self_demu()
# a.methodb()

# operator overloading example
# class overload:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c=0):
#         print(a+b+c)
# p = overload()
# print(p.add(10,20,20))

# single level inheritance
# class point_1:
#     def set_cord(self,x,y):
#         print(f"x axis is: {x} and y axis is: {y}")
# class new_point(point_1):
#     def draw(self,x,y):
#         print(x+y)
# a = new_point()
# print(a.new_point.point_1.set_cord(2,3))

# # multi level inheritance
# class student:
#     name ="shil"
# class parent(student):
#     father_name = "lava"
# class school(parent):
#     def details(self):
#         print(self.name,self.father_name)
# c = school()
# c.details()

#  multiple inheritance
# class grandfather:
#     grandfather_name = "qwert"
#     def get_grand1(self):
#         print(self.grandfather_name)
# class grandmother:
#     grandmother_name = "asdfg"
#     def grad_grand2(self):
#         print(self.grandmother_name)
# class son(grandmother,grandfather):
#     name = "karl"
#     def son_name(self):
#         print(self.name)
# c = son()
# c.grad_grand2()
# c.get_grand1()
