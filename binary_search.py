def binary_search(items, key):
    # Search an already sorted list
    left = 0
    right = len(items) - 1

    # Continue while a search range remains
    while left <= right:

        # Choose the middle index
        mid = (left + right) // 2

        # Check whether the middle value is the key
        if items[mid] == key:
            return mid

        # If middle value is too small, search the right half
        if items[mid] < key:
            left = mid + 1

        # Otherwise, search the left half
        else:
            right = mid - 1

    # Key was not found
    return -1


# Sorted list
numbers = [2, 4, 6, 8, 10]

# Search for a present key
print(binary_search(numbers, 8))

# Search for an absent key
print(binary_search(numbers, 9))
def binary_search(items, key):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == key:
            return mid

        if items[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Sorted list containing duplicates
numbers = [2, 4, 6, 6, 6, 8, 10]

# Search for the duplicated value
index = binary_search(numbers, 6)

print("Matching index:", index)
print("Matching value:", numbers[index])
