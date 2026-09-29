import heapq


def prim(graph, start):
    # Start with one vertex
    visited = {start}

    # Add all edges from the starting vertex
    heap = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start]
    ]

    # Arrange edges by weight
    heapq.heapify(heap)

    # Store MST edges
    chosen = []

    while heap and len(visited) < len(graph):
        # Select the cheapest frontier edge
        weight, u, v = heapq.heappop(heap)

        # Skip if the vertex is already in the MST
        if v in visited:
            continue

        # Add the new vertex
        visited.add(v)

        # Add the selected edge to the MST
        chosen.append((u, v, weight))

        # Add new frontier edges
        for neighbor, cost in graph[v]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost, v, neighbor))

    # Check whether all vertices were reached
    if len(visited) != len(graph):
        raise ValueError("Graph is disconnected")

    # Return MST edges and total weight
    return chosen, sum(w for _, _, w in chosen)


# Undirected weighted graph
graph = {
    "A": [("B", 1), ("C", 3)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 3), ("B", 2), ("D", 4)],
    "D": [("B", 5), ("C", 4)]
}


# Find MST starting from A
print(prim(graph, "A"))
import heapq


def prim(graph, start):
    visited = {start}

    # Add starting vertex's edges to the priority queue
    heap = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start]
    ]
    heapq.heapify(heap)

    chosen = []

    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)

        if v in visited:
            continue

        visited.add(v)
        chosen.append((u, v, weight))

        # Add edges from the newly visited vertex
        for neighbor, cost in graph[v]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost, v, neighbor))

    if len(visited) != len(graph):
        raise ValueError("Graph is disconnected")

    return chosen, sum(w for _, _, w in chosen)


# Undirected weighted graph
graph = {
    "A": [("B", 1), ("C", 3)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 3), ("B", 2), ("D", 4)],
    "D": [("B", 5), ("C", 4)]
}


# Prim starting from A
mst_a, total_a = prim(graph, "A")

# Prim starting from D
mst_d, total_d = prim(graph, "D")

print("Starting from A:")
print("Edges:", mst_a)
print("Total:", total_a)

print("\nStarting from D:")
print("Edges:", mst_d)
print("Total:", total_d)

print("\nSame total:", total_a == total_d)
print("Same edge set:",
      {frozenset((u, v)) for u, v, w in mst_a}
      == {frozenset((u, v)) for u, v, w in mst_d})
