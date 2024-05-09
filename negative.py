def remove_negative(a):
    positive = []

    for element in a:
        if element >= 0:
            positive.append(element)

    return positive

a = [-1, 0, 1, -2]
result = remove_negative(a)
print("Original List:", a)
print("Positive Elements:", result)
