class Node:
    # Store AVL key, children and height
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(n):
    # Read height safely
    return n.height if n else 0


def update(n):
    # Recompute height after a change
    n.height = 1 + max(height(n.left), height(n.right))


def rotate_right(y):
    # Repair a left-heavy subtree
    x = y.left
    middle = x.right

    x.right = y
    y.left = middle

    update(y)
    update(x)

    return x


def rotate_left(x):
    # Repair a right-heavy subtree
    y = x.right
    middle = y.left

    y.left = x
    x.right = middle

    update(x)
    update(y)

    return y


def insert(n, key):
    # Insert and restore AVL balance
    if n is None:
        return Node(key)

    if key < n.key:
        n.left = insert(n.left, key)

    elif key > n.key:
        n.right = insert(n.right, key)

    else:
        return n  # Ignore duplicates

    update(n)

    balance = height(n.left) - height(n.right)

    # Left-Left or Left-Right case
    if balance > 1:
        if key > n.left.key:
            n.left = rotate_left(n.left)

        return rotate_right(n)

    # Right-Right or Right-Left case
    if balance < -1:
        if key < n.right.key:
            n.right = rotate_right(n.right)

        return rotate_left(n)

    return n


# Start with an empty AVL tree
root = None

# Insert values to trigger LL rotation
for key in [30, 20, 10]:
    root = insert(root, key)

# Print the balanced tree
print("Root:", root.key)
print("Left child:", root.left.key)
print("Right child:", root.right.key)
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(n):
    return n.height if n else 0


def update(n):
    n.height = 1 + max(height(n.left), height(n.right))


def rotate_right(y):
    x = y.left
    middle = x.right

    x.right = y
    y.left = middle

    update(y)
    update(x)

    return x


def rotate_left(x):
    y = x.right
    middle = y.left

    y.left = x
    x.right = middle

    update(x)
    update(y)

    return y


def insert(n, key):
    if n is None:
        return Node(key)

    if key < n.key:
        n.left = insert(n.left, key)
    elif key > n.key:
        n.right = insert(n.right, key)
    else:
        return n

    update(n)

    balance = height(n.left) - height(n.right)

    # Left-Left case
    if balance > 1 and key < n.left.key:
        return rotate_right(n)

    # Left-Right case
    if balance > 1 and key > n.left.key:
        n.left = rotate_left(n.left)
        return rotate_right(n)

    # Right-Right case
    if balance < -1 and key > n.right.key:
        return rotate_left(n)

    # Right-Left case
    if balance < -1 and key < n.right.key:
        n.right = rotate_right(n.right)
        return rotate_left(n)

    return n


def test_sequence(values):
    root = None

    for value in values:
        root = insert(root, value)

    return root.key


# Test all three insertion sequences
sequences = [
    [30, 10, 20],
    [10, 20, 30],
    [10, 30, 20]
]

for sequence in sequences:
    new_root = test_sequence(sequence)
    print(sequence, "-> New root:", new_root)
