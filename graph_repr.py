vertices = ["A", "B", "C"]

# Undirected edges
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C")
]

# Create adjacency list
graph = {v: [] for v in vertices}

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Map vertex names to matrix indices
index = {v: i for i, v in enumerate(vertices)}

# Create adjacency matrix
matrix = [[0] * len(vertices) for _ in vertices]

for u, v in edges:
    matrix[index[u]][index[v]] = 1
    matrix[index[v]][index[u]] = 1

# Print adjacency list
print("Adjacency List:")
print(graph)

# Print adjacency matrix
print("\nAdjacency Matrix:")
for row in matrix:
    print(row)
vertices = ["A", "B", "C"]

# Undirected edges after removing B-C
edges = [
    ("A", "B"),
    ("A", "C")
]

# Create adjacency list
graph = {v: [] for v in vertices}

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Map vertices to matrix indices
index = {v: i for i, v in enumerate(vertices)}

# Create adjacency matrix
matrix = [[0] * len(vertices) for _ in vertices]

for u, v in edges:
    matrix[index[u]][index[v]] = 1
    matrix[index[v]][index[u]] = 1

# Print adjacency list
print("Adjacency List:")
print(graph)

# Print adjacency matrix
print("\nAdjacency Matrix:")
for row in matrix:
    print(row)
