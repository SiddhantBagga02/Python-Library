# import re
# pattern=r"SAHIL"
# file_path=r"C:\Users\nm639\Desktop\python\alt.txt"                        
# f = open(file_path,"r")                                                   
# file = f.read()
# # match = re.search(pattern,file)
# # flags is used to ignore case sensitive letters   
# match = re.search(pattern,file,re.IGNORECASE)        

# if match:
#     print("found")
# else:
#     print("not found")
# print(match)


# # re object
# import re
# pattern = re.compile("il",re.IGNORECASE)
# file_path=r"C:\Users\nm639\Desktop\python\alt.txt"
# f = open(file_path,"r")
# file = f.read()
# m = re.finditer(pattern,file)  
# # counting no of times patter occurs
# count = 0
# # to get index use start and to print the patter use match
# for item in m:
#     count+=1
#     x = item.group()
#     print(item.group(),"is found at: ",item.start())
# print(f"total no of times {x} occurs: ",count)

# # using finall
# import re
# pattern = re.compile("il",re.IGNORECASE)
# file_path=r"C:\Users\nm639\Desktop\python\alt.txt"
# f = open(file_path,"r")
# file = f.read()
# m = re.findall(pattern,file)  
# # counting no of times patter occurs
# i = 0
# count = 0
# for item in m:
#     print(m[i])
#     i+=1
#     count+=1
# print(f"no of times pattern occurs: ",count)


# # used to find non over lapping matches
# import re
# pattern = re.compile("kk",re.IGNORECASE)
# file_path=r"C:\Users\nm639\Desktop\python\alt.txt"
# f = open(file_path,"r")
# file = f.read()
# m = re.finditer(pattern,file)  
# # counting no of times patter occurs
# count = 0
# # to get index use start and to print the patter use match
# for item in m:
#     count+=1
#     x = item.group()
#     print(item.group(),"is found at: ",item.start())
# print(f"total no of times {x} occurs: ",count)

# used to find non over lapping matches
# import re
# pattern = re.compile("kk",re.IGNORECASE)
# file_path=r"C:\Users\nm639\Desktop\python\alt.txt"
# f = open(file_path,"r")
# file = f.read()
# m = re.findall(pattern,file)  
# # counting no of times patter occurs
# i = 0
# count = 0
# for item in m:
#     print(m[i])
#     i+=1
#     count+=1
# print(f"no of times pattern occurs: ",count)

# def sum_of_salary(file_path):
#     import re
#     pattern = re.compile('\d+')
#     # file_path=r"C:\Users\nm639\Desktop\python\alt.txt"
#     f = open(file_path,"r")
#     file = f.read()
#     m = re.findall(pattern,file)
#     print(m)
#     sum = 0
#     i = 0
#     for item in m:
#         sum+=m[i]
#         i+=1
#     return sum
#     print(sum)

# sum_of_salary("C:/Users/nm639/Desktop/python/alt.txt")



# def sum_of_salary(file_path):
#     import re
#     pattern = re.compile(r"\d+")
#     # file_path=r"C:\Users\nm639\Desktop\python\alt.txt"
#     f = open(file_path,"r")
#     file = f.read()
#     m = re.findall(pattern,file)
#     print(m)
#     sum = 0
#     i = 0
#     for item in m:
#         sum+=int(m[i])
#         i+=1
#     return sum
#     print(sum)

# # Call the function with a valid file path
# file_path = r"C:\Users\nm639\Desktop\python\alt.txt"
# print(sum_of_salary(file_path))






    

 

    









