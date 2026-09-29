class Node:
    # A node holding one BST value
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    # Return the updated root
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)

    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def contains(root, value):
    # Test membership
    while root is not None:
        if value == root.value:
            return True

        if value < root.value:
            root = root.left
        else:
            root = root.right

    return False


def inorder(root):
    # Display sorted BST keys
    if root is None:
        return []

    return inorder(root.left) + [root.value] + inorder(root.right)


# Start with an empty tree
root = None

# Insert keys in order
for key in [8, 3, 10, 1, 6]:
    root = insert(root, key)

# Print sorted keys
print(inorder(root))

# Check whether values exist
print(contains(root, 6), contains(root, 9))
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    if root is None:
        return []

    return inorder(root.left) + [root.value] + inorder(root.right)


# Create a new empty tree
root = None

# Insert sorted values
for value in [1, 2, 3, 4, 5]:
    root = insert(root, value)

# Display the tree using inorder traversal
print("Inorder:", inorder(root))

# The tree becomes skewed
print("Tree becomes slow because it behaves like a linked list.")
print("Search and insertion can take O(n) time.")
