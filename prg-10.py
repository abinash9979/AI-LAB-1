from itertools import permutations

def tsp(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)

    min_cost = float('inf')
    best_path = None

    for path in permutations(cities):
        current_path = [start] + list(path) + [start]

        cost = 0

        for i in range(len(current_path) - 1):
            cost += graph[current_path[i]][current_path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = current_path

    return best_path, min_cost


# Cost matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start = 0

path, cost = tsp(graph, start)

print("Shortest Path:", path)
print("Minimum Cost:", cost)