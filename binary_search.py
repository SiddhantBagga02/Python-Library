def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        # Check if the target is equal to the middle element
        if mid_value == target:
            return mid
        # If the target is smaller, ignore the right half
        elif mid_value > target:
            high = mid - 1
        # If the target is larger, ignore the left half
        else:
            low = mid + 1

    # If the target is not in the array
    return -1

# Example usage:
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_value = 7

    result = binary_search(sorted_array, target_value)

    if result != -1:
        print(f"Element {target_value} is present at index {result}.")
    else:
        print(f"Element {target_value} is not present in the array.")
