def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Function call
dfs(graph, 'A')
        