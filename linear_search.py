def linear_search(items, key):
    # Check each item from left to right
    for i, value in enumerate(items):

        # Check whether the current value matches the key
        if value == key:
            return i

    # Key was not found
    return -1


# Unsorted input list
numbers = [8, 3, 11, 5]

# Search for a value that exists
print(linear_search(numbers, 11))

# Search for a value that does not exist
print(linear_search(numbers, 7))
def linear_search(items, key):
    comparisons = 0

    for i, value in enumerate(items):
        comparisons += 1

        if value == key:
            return i, comparisons

    return -1, comparisons


# Unsorted input list
numbers = [8, 3, 11, 5]

# Search for 8
index_8, comparisons_8 = linear_search(numbers, 8)

# Search for 5
index_5, comparisons_5 = linear_search(numbers, 5)

print("Search for 8:")
print("Index:", index_8)
print("Comparisons:", comparisons_8)

print("\nSearch for 5:")
print("Index:", index_5)
print("Comparisons:", comparisons_5)
