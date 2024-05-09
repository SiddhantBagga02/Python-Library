def is_prime(element):
    if element < 2:
        return False
    for i in range(2, int(element**0.5) + 1):
        if element % i == 0:
            return False
    return True

def prime(a):
    prime_check_list = [is_prime(element) for element in a]
    return prime_check_list

# Example usage:
my_list = [2, 7, 4, 11, 6, 13]
result = prime(my_list)

print("Original List:", my_list)
print("Prime Check List:", result)
