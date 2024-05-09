def duplicate(a):
    duplicate_list = []
    for element in a:
        duplicate_list.append(element)
        duplicate_list.append(element)

    return duplicate_list

a = [1,2,3]
result = duplicate(a)
print(a)
print(result)


