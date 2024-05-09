# Q1) write a python program  to create a class name circle. pass the parameter radius to the method named crc_area ?
# class circle:
#     def crc_area(self,radius):
#         if radius <= 0:
#             return "please enter a valid number"
#         area = 3.14*(radius**2)
#         return area
# obj = circle()
# print("area of cicle is: ",obj.crc_area(10))



# Q2) write a pythong programe to create a class named demo. define two method get_string and print_string. accept the string from user and print the string in upper case

class demo:
    def get_string(self):   
        self.o = input('entre your name: ')
    def print_string(self):
        b = self.o.upper()
        print("your string",b)

obj = demo()
obj.get_string()
obj.print_string()


    