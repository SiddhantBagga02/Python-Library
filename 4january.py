#                                    --4TH JANUARY PY PROGRAMS--
# ___________________________________________________________________________________________________




# # write a python program to read first n lines of a file ?

# def read_first_n_lines(file_path,n):
#     with open(file_path,'r') as file:
#          lines = file.readlines()
#          return lines[:n]
# file_path = "C:/Users/nm639/Desktop/python/alt.txt"
# n = 1
# result = read_first_n_lines(file_path,n)
# print(result)
# ------------------------------------------------------------------------------------------------
# write a python program that match a string starting with a followed by 3b ex abbb ?

# import re
# filename = "alt.txt"
# search_string = "abbb"
# with open(filename, 'r') as f:
#   for line in f:
#     if re.search(search_string, line):
#       print(line)
# -------------------------------------------------------------------------------------------------
#  write a program to check wether last digit of a number is divisible by 3 or not?

# --------------------------------------------------------------------------------------------------
# write a py program to find longest word in a file ?

# def longest_word(filename):
#   with open(filename, 'r') as f:   
#     longest = ''   
#     for line in f:      
#       words = line.split()     
#       for word in words:        
#         if len(word) > len(longest):
#           longest = word    
#     return longest
# print(longest_word('alt.txt'))
# ---------------------------------------------------------------------------------------------------
#  write a program to label days from 1 to 7

# ------------------------------------------------------------------------------------------