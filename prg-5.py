import heapq
def heuristic(node, goal):
    h = {
        'A': 6,
        'B': 4,
        'C': 3,
        'D': 1,
        'E': 0
    }
    return h[node]

def reconstruct_path(parent, current):
    path = []

    while current is not None:
        path.insert(0, current)
        current = parent[current]

    return path

def a_star(graph, start, goal):
    openlist = []
    closedlist = set()

    g = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    g[start] = 0

    f = g[start] + heuristic(start, goal)
    heapq.heappush(openlist, (f, start))

    while openlist:
        current_f, current = heapq.heappop(openlist)

        if current in closedlist:
            continue

        if current == goal:
            return reconstruct_path(parent, current)

        closedlist.add(current)

        for neighbor, distance in graph[current]:

            if neighbor in closedlist:
                continue

            tentative_g = g[current] + distance

            if tentative_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = tentative_g

                f = g[neighbor] + heuristic(neighbor, goal)

                heapq.heappush(openlist, (f, neighbor))

    return None

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3), ('E', 5)],
    'C': [('A', 4), ('D', 2)],
    'D': [('B', 3), ('C', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1)]
}

start = 'A'
goal = 'E'

path = a_star(graph, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
else:
    print("No path found")