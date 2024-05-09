def count_occurrences(lst):
    occurrences = {}

    for element in lst:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    for element, count in occurrences.items():
        print(f"{element} occurred {count} times")

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 3, 5]
count_occurrences(my_list)
