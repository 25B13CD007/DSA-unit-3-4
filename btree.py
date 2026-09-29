class Node:
    # A B-tree node holding several keys
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree:
    # Minimum degree 2: at most three keys per node
    def __init__(self):
        self.root = Node()

    def split(self, parent, index):
        # Split one full child
        full = parent.children[index]

        right = Node(full.leaf)

        # Median moves upward
        middle = full.keys[1]

        # Larger keys move right
        right.keys = full.keys[2:]

        # Smaller key stays left
        full.keys = full.keys[:1]

        if not full.leaf:
            right.children = full.children[2:]
            full.children = full.children[:2]

        # Promote median
        parent.keys.insert(index, middle)

        # Attach right sibling
        parent.children.insert(index + 1, right)

    def insert_nonfull(self, node, key):
        # Descend into a non-full node
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
            return

        i = 0

        # Find the correct child
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # Split full child before descending
        if len(node.children[i].keys) == 3:
            self.split(node, i)

            # Choose the correct side after splitting
            if key > node.keys[i]:
                i += 1

        self.insert_nonfull(node.children[i], key)

    def insert(self, key):
        # Reject duplicate keys
        if self.search(self.root, key):
            return

        # If root is full, split it
        if len(self.root.keys) == 3:
            old = self.root

            self.root = Node(False)
            self.root.children = [old]

            self.split(self.root, 0)

        self.insert_nonfull(self.root, key)

    def search(self, node, key):
        # Search for a key
        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(node.children[i], key)

    def levels(self):
        # Display the tree level by level
        queue = [self.root]

        while queue:
            print([node.keys for node in queue])

            queue = [
                child
                for node in queue
                for child in node.children
            ]


# Create a B-tree
bt = BTree()

# Insert test keys
for key in [10, 20, 5, 6]:
    bt.insert(key)

# Display the B-tree structure
bt.levels()

# Search for keys
print("Search 6:", bt.search(bt.root, 6))
print("Search 9:", bt.search(bt.root, 9))
class Node:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree:
    # Minimum degree = 2
    # Maximum 3 keys per node
    def __init__(self):
        self.root = Node()

    def split(self, parent, index):
        full = parent.children[index]

        right = Node(full.leaf)

        # Promote the middle key
        middle = full.keys[1]

        # Move larger key(s) to the right node
        right.keys = full.keys[2:]

        # Keep smaller key(s) in the left node
        full.keys = full.keys[:1]

        # Move children if this is an internal node
        if not full.leaf:
            right.children = full.children[2:]
            full.children = full.children[:2]

        parent.keys.insert(index, middle)
        parent.children.insert(index + 1, right)

    def insert_nonfull(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
            return

        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # Split full child before descending
        if len(node.children[i].keys) == 3:
            self.split(node, i)

            if key > node.keys[i]:
                i += 1

        self.insert_nonfull(node.children[i], key)

    def insert(self, key):
        # Ignore duplicates
        if self.search(self.root, key):
            return

        # Split full root
        if len(self.root.keys) == 3:
            old = self.root

            self.root = Node(False)
            self.root.children = [old]

            self.split(self.root, 0)

        self.insert_nonfull(self.root, key)

    def search(self, node, key):
        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(node.children[i], key)

    def levels(self):
        # Print tree level by level
        queue = [self.root]

        while queue:
            print([node.keys for node in queue])

            queue = [
                child
                for node in queue
                for child in node.children
            ]


# Create B-tree
bt = BTree()

# Original keys
for key in [10, 20, 5, 6]:
    bt.insert(key)

print("After inserting 10, 20, 5, 6:")
bt.levels()

# Continue inserting keys
for key in [12, 30, 7, 17]:
    bt.insert(key)

print("\nAfter inserting 12, 30, 7, 17:")
bt.levels()

# Search tests
print("\nSearch results:")
print("6:", bt.search(bt.root, 6))
print("9:", bt.search(bt.root, 9))
print("17:", bt.search(bt.root, 17))
print("30:", bt.search(bt.root, 30))
