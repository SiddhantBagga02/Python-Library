# try :
#     10 = (1/0)
# except :
#     print("the calculation failed")
# x = 2
# try:
#     print(x)
# except name_error:
#     print("x is not defined")
# except :
#     print("something is wrong")
# finally:
#     print("the program is finished")

try:
    result = 10/2
except ZeroDivisionError:
    print("The calculation failed")
# x = 2
try:
    print(x)
except NameError:
    print("x is not defined")
except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    print("The program is finished")
