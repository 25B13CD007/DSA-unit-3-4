def radix_sort(a):
    # Sort non-negative integers by digits
    if any(x < 0 for x in a):
        raise ValueError("Use non-negative integers")

    # Start with the units digit
    place = 1

    # Find the largest value
    maximum = max(a, default=0)

    # Process each digit position
    while maximum // place > 0:
        # Create 10 buckets for digits 0-9
        buckets = [[] for _ in range(10)]

        # Put each value into its digit bucket
        for value in a:
            digit = (value // place) % 10
            buckets[digit].append(value)

        # Flatten buckets while preserving order
        a = [
            value
            for bucket in buckets
            for value in bucket
        ]

        # Move to the next digit
        place *= 10

    return a


# Test the radix sort
numbers = [21, 13, 12]

print(radix_sort(numbers))
def radix_sort(a):
    # Reject negative numbers
    if any(x < 0 for x in a):
        raise ValueError("Use non-negative integers")

    place = 1
    maximum = max(a, default=0)
    pass_number = 1

    while maximum // place > 0:
        buckets = [[] for _ in range(10)]

        # Place values into buckets based on current digit
        for value in a:
            digit = (value // place) % 10
            buckets[digit].append(value)

        # Flatten buckets
        a = [
            value
            for bucket in buckets
            for value in bucket
        ]

        print(f"Pass {pass_number} ({place}s digit):", a)

        place *= 10
        pass_number += 1

    return a


# Test input
numbers = [5, 105, 15, 0]

print("Input:", numbers)
print("Sorted:", radix_sort(numbers))
 