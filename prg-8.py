from collections import deque


def water_jug(cap1, cap2, target_state):

    visited = set()
    queue = deque()

    # Start with both jugs empty
    queue.append((0, 0, []))
    visited.add((0, 0))

    while queue:
        jug1, jug2, path = queue.popleft()

        # Check if target is reached
        if (jug1, jug2) == target_state:
            return path + [(jug1, jug2)]

        # Possible states
        states = [
            (cap1, jug2),              # Fill Jug 1
            (jug1, cap2),              # Fill Jug 2
            (0, jug2),                 # Empty Jug 1
            (jug1, 0),                 # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (
                jug1 - min(jug1, cap2 - jug2),
                jug2 + min(jug1, cap2 - jug2)
            ),
            # Pour Jug 2 -> Jug 1
            (
                jug1 + min(jug2, cap1 - jug1),
                jug2 - min(jug2, cap1 - jug1)
            )
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [(jug1, jug2)]))

    return None


# Jug capacities
cap1 = 4
cap2 = 3

# Target state
target_state = (2, 0)

solution = water_jug(cap1, cap2, target_state)

if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution exists.")