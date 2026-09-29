from collections import deque
# Imports deque, which provides an efficient FIFO queue.


def bfs(graph, start):
    # Defines the BFS function.
    # graph is the graph, and start is the starting vertex.

    queue = deque([start])
    # Creates a queue and puts the starting vertex into it.

    seen = {start}
    # Keeps track of visited vertices.
    # The start vertex is marked immediately.

    order = []
    # Creates a list to store the order in which vertices are visited.

    while queue:
        # Continues as long as the queue is not empty.

        node = queue.popleft()
        # Removes the oldest vertex from the front of the queue.

        order.append(node)
        # Adds the current vertex to the BFS traversal order.

        for neighbor in graph[node]:
            # Examines every neighbor of the current vertex.

            if neighbor not in seen:
                # Checks whether the neighbor has already been visited.

                seen.add(neighbor)
                # Marks the neighbor as visited.

                queue.append(neighbor)
                # Adds the neighbor to the back of the queue.

    return order
    # Returns the final BFS traversal order.


# Define the graph using an adjacency list.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}


# Start BFS from vertex A.
result = bfs(graph, "A")

# Print the BFS traversal.
print(result)
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    seen = {start}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return order


# Graph with isolated vertex E
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
    "E": []
}


# BFS starts at A
print("BFS from A:", bfs(graph, "A"))

# BFS starts at E
print("BFS from E:", bfs(graph, "E"))
