def dfs(graph, start):
    # Track visited vertices
    seen = set()

    # Store the traversal order
    order = []

    def visit(node):
        # Stop if the vertex was already visited
        if node in seen:
            return

        # Mark the vertex as visited
        seen.add(node)

        # Record the first visit
        order.append(node)

        # Visit each neighbor in listed order
        for neighbor in graph[node]:
            visit(neighbor)

    # Start DFS from the given vertex
    visit(start)

    # Return the traversal order
    return order


# Define the graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}


# Run DFS starting from A
print(dfs(graph, "A"))
def dfs(graph, start):
    seen = set()
    order = []

    def visit(node):
        if node in seen:
            return

        seen.add(node)
        order.append(node)

        for neighbor in graph[node]:
            visit(neighbor)

    visit(start)

    return order


# Graph with A's neighbors reversed
graph = {
    "A": ["C", "B"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}


# Run DFS from A
print("DFS order:", dfs(graph, "A"))
