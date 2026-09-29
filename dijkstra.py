import heapq


def dijkstra(graph, start):
    # Set initial distances to infinity
    distance = {v: float("inf") for v in graph}

    # Distance from start to itself is zero
    distance[start] = 0

    # Priority queue: (distance, vertex)
    heap = [(0, start)]

    while heap:
        # Get the vertex with the smallest distance
        cost, u = heapq.heappop(heap)

        # Ignore an outdated heap entry
        if cost != distance[u]:
            continue

        # Check all outgoing edges
        for v, weight in graph[u]:

            # Dijkstra requires non-negative weights
            if weight < 0:
                raise ValueError("Negative edge")

            # Calculate distance through u
            candidate = cost + weight

            # Update if a shorter path is found
            if candidate < distance[v]:
                distance[v] = candidate
                heapq.heappush(heap, (candidate, v))

    return distance


# Directed weighted graph
g = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1)],
    "C": [("B", 2), ("D", 5)],
    "D": []
}


# Find shortest distances from A
print(dijkstra(g, "A"))
import heapq


def dijkstra(graph, start):
    distance = {v: float("inf") for v in graph}
    distance[start] = 0

    heap = [(0, start)]

    while heap:
        cost, u = heapq.heappop(heap)

        if cost != distance[u]:
            continue

        for v, weight in graph[u]:
            if weight < 0:
                raise ValueError("Negative edge")

            candidate = cost + weight

            if candidate < distance[v]:
                distance[v] = candidate
                heapq.heappush(heap, (candidate, v))

    return distance


# Directed weighted graph
g = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1)],
    "C": [("B", 2), ("D", 2)],  # New C -> D edge
    "D": []
}


# Find shortest distances from A
distances = dijkstra(g, "A")

print("Shortest distances:", distances)
print("Shortest distance to D:", distances["D"])
