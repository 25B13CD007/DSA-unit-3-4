def kruskal(vertices, edges):
    # Each vertex starts in its own component
    parent = {v: v for v in vertices}

    def find(x):
        # Find the representative of a component
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    chosen = []

    # Process edges from smallest to largest weight
    for weight, u, v in sorted(edges):
        a = find(u)
        b = find(v)

        # Add edge only if it does not create a cycle
        if a != b:
            parent[a] = b
            chosen.append((u, v, weight))

    # A connected graph with V vertices needs V-1 edges
    if len(chosen) != len(vertices) - 1:
        raise ValueError("Graph is disconnected")

    # Return selected edges and total weight
    return chosen, sum(w for _, _, w in chosen)


# Four campuses
vertices = ["A", "B", "C", "D"]

# Undirected weighted edges
edges = [
    (1, "A", "B"),
    (2, "B", "C"),
    (3, "A", "C"),
    (4, "C", "D"),
    (5, "B", "D")
]

# Find and display the minimum spanning tree
print(kruskal(vertices, edges))
def kruskal(vertices, edges):
    # Each vertex starts in its own component
    parent = {v: v for v in vertices}

    def find(x):
        # Find the component representative
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    chosen = []

    # Sort edges by weight
    for weight, u, v in sorted(edges):
        a = find(u)
        b = find(v)

        # Choose the edge if it does not create a cycle
        if a != b:
            parent[a] = b
            chosen.append((u, v, weight))

    if len(chosen) != len(vertices) - 1:
        raise ValueError("Graph is disconnected")

    return chosen, sum(w for _, _, w in chosen)


# Vertices
vertices = ["A", "B", "C", "D"]

# AC changed from weight 3 to weight 1
edges = [
    (1, "A", "B"),
    (1, "A", "C"),
    (2, "B", "C"),
    (4, "C", "D"),
    (5, "B", "D")
]

# Calculate MST
chosen, total = kruskal(vertices, edges)

print("Chosen edges:", chosen)
print("Total weight:", total)
