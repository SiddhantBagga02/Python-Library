def even(a):
    even_elements = []
    for element in a:
        if element%2 == 0:
            even_elements.append(element)
    
    return even_elements

a = [2,3,4,5,6,7]
result = even(a)
print(a)
print(result)