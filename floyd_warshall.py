def floyd_warshall(vertices, edges):
    # Represent unreachable pairs
    inf = float("inf")

    # Create the distance matrix
    dist = {
        u: {
            v: (0 if u == v else inf)
            for v in vertices
        }
        for u in vertices
    }

    # Add directed edges
    for u, v, weight in edges:
        # Keep the cheapest parallel edge
        dist[u][v] = min(dist[u][v], weight)

    # Try every vertex as an intermediate vertex
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    # Check for a negative cycle
    if any(dist[v][v] < 0 for v in vertices):
        raise ValueError("Negative cycle")

    return dist


# Vertex names
names = ["A", "B", "C"]

# Directed weighted edges
edges = [
    ("A", "B", 3),
    ("B", "C", 2),
    ("A", "C", 10)
]

# Calculate all-pairs shortest distances
result = floyd_warshall(names, edges)

# Print the distance matrix
for name in names:
    print(name, [result[name][v] for v in names])
def floyd_warshall(vertices, edges):
    inf = float("inf")

    # Create distance matrix
    dist = {
        u: {
            v: (0 if u == v else inf)
            for v in vertices
        }
        for u in vertices
    }

    # Add edges
    for u, v, weight in edges:
        dist[u][v] = min(dist[u][v], weight)

    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    # Check for negative cycles
    if any(dist[v][v] < 0 for v in vertices):
        raise ValueError("Negative cycle")

    return dist


# Vertices
names = ["A", "B", "C"]

# Directed weighted edges
edges = [
    ("A", "B", 3),
    ("B", "C", 2),
    ("A", "C", 10),
    ("C", "A", 1)       # New edge
]

# Calculate shortest distances
result = floyd_warshall(names, edges)

# Display distance matrix
for name in names:
    print(name, [result[name][v] for v in names])
