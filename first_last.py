def remove_first_last(lst):
    if len(lst) >= 2:
        lst.pop(0)  
        lst.pop(-1)  
    else:
        print("List has less than two elements. Cannot remove first and last.")


my_list = [1, 2, 3, 4, 5]
remove_first_last(my_list)

print("Original List:", my_list)
