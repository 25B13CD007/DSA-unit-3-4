class Node:
    # Represent one binary-tree position
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(node):
    # Visit left, root, right
    if node is None:
        return []

    return inorder(node.left) + [node.value] + inorder(node.right)


def preorder(node):
    # Visit root, left, right
    if node is None:
        return []

    return [node.value] + preorder(node.left) + preorder(node.right)


def postorder(node):
    # Visit left, right, root
    if node is None:
        return []

    return postorder(node.left) + postorder(node.right) + [node.value]


# Create the binary tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)

# Print the traversals
print("Inorder:", inorder(root))
print("Preorder:", preorder(root))
print("Postorder:", postorder(root))
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


root = Node(8)
root.left = Node(3)
root.right = Node(10)

# Attach 1 as the left child of 3
root.left.left = Node(1)

print("Inorder:", inorder(root))
print("Preorder:", preorder(root))
print("Postorder:", postorder(root))
