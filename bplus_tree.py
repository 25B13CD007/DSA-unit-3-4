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

        # Promote middle key
        middle = full.keys[1]

        # Move larger key to right node
        right.keys = full.keys[2:]

        # Keep smaller key in left node
        full.keys = full.keys[:1]

        # Move children if internal node
        if not full.leaf:
            right.children = full.children[2:]
            full.children = full.children[:2]

        # Insert promoted key and new child
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

        # Split full child
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

# Insert initial keys
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

        # Promote middle key
        middle = full.keys[1]

        # Larger keys move right
        right.keys = full.keys[2:]

        # Smaller key stays left
        full.keys = full.keys[:1]

        # Move children if internal node
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
        queue = [self.root]

        while queue:
            print([node.keys for node in queue])

            queue = [
                child
                for node in queue
                for child in node.children
            ]


# -------------------------------------------------
# Bulk-load demonstration
# -------------------------------------------------

# Original data
keys = [10, 20, 5, 6, 12, 30, 7, 17]

print("Original B-tree:")
bt = BTree()

for key in keys:
    bt.insert(key)

bt.levels()


# Add 20 to the data and REBUILD the entire index
# This is NOT an insertion into the existing live tree.
keys.append(20)

print("\nRebuilt B-tree after adding 20:")

rebuilt_bt = BTree()

for key in keys:
    rebuilt_bt.insert(key)

rebuilt_bt.levels()


# Search after rebuilding
print("\nSearch results:")
print("6:", rebuilt_bt.search(rebuilt_bt.root, 6))
print("20:", rebuilt_bt.search(rebuilt_bt.root, 20))
print("25:", rebuilt_bt.search(rebuilt_bt.root, 25))
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

        # Promote middle key
        middle = full.keys[1]

        # Larger keys move right
        right.keys = full.keys[2:]

        # Smaller key stays left
        full.keys = full.keys[:1]

        # Move children if internal node
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
        queue = [self.root]

        while queue:
            print([node.keys for node in queue])

            queue = [
                child
                for node in queue
                for child in node.children
            ]


# -------------------------------------------------
# Bulk-load demonstration
# -------------------------------------------------

# Original data
keys = [10, 20, 5, 6, 12, 30, 7, 17]

print("Original B-tree:")
bt = BTree()

for key in keys:
    bt.insert(key)

bt.levels()


# Add 20 to the data and REBUILD the entire index
# This is NOT an insertion into the existing live tree.
keys.append(20)

print("\nRebuilt B-tree after adding 20:")

rebuilt_bt = BTree()

for key in keys:
    rebuilt_bt.insert(key)

rebuilt_bt.levels()


# Search after rebuilding
print("\nSearch results:")
print("6:", rebuilt_bt.search(rebuilt_bt.root, 6))
print("20:", rebuilt_bt.search(rebuilt_bt.root, 20))
print("25:", rebuilt_bt.search(rebuilt_bt.root, 25))
