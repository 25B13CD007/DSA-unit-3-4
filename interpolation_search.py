def interpolation_search(a, key):
    # Search a sorted list of numeric values
    low = 0
    high = len(a) - 1

    # Continue while key is within the current range
    while low <= high and a[low] <= key <= a[high]:

        # Avoid division by zero
        if a[low] == a[high]:
            return low if a[low] == key else -1

        # Estimate the likely position of the key
        pos = low + (
            (key - a[low]) * (high - low)
            // (a[high] - a[low])
        )

        # Key found
        if a[pos] == key:
            return pos

        # Key is larger, search the right side
        if a[pos] < key:
            low = pos + 1

        # Key is smaller, search the left side
        else:
            high = pos - 1

    # Key was not found
    return -1


# Sorted numeric list
numbers = [10, 20, 30, 40, 50]

# Search for a present value
print(interpolation_search(numbers, 40))

# Search for an absent value
print(interpolation_search(numbers, 35))
def interpolation_search(a, key):
    low = 0
    high = len(a) - 1

    while low <= high and a[low] <= key <= a[high]:

        # All values in the current range are equal
        if a[low] == a[high]:
            return low if a[low] == key else -1

        # Estimate the position
        pos = low + (
            (key - a[low]) * (high - low)
            // (a[high] - a[low])
        )

        if a[pos] == key:
            return pos

        if a[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# All elements are equal
numbers = [7, 7, 7]

# Search for 7
print("Search 7:", interpolation_search(numbers, 7))

# Search for 8
print("Search 8:", interpolation_search(numbers, 8))
