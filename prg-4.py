def minimax(depth, nodeindex, isMax, scores, height):

    if depth == height:
        return scores[nodeindex]

    if isMax:
        return max(
            minimax(depth + 1, nodeindex * 2, False, scores, height),
            minimax(depth + 1, nodeindex * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeindex * 2, True, scores, height),
            minimax(depth + 1, nodeindex * 2 + 1, True, scores, height)
        )


scores = list(map(int, input("Enter 8 leaf node values: ").split()))

height = 3
result = minimax(0, 0, True, scores, height)
print("\nThe optimal value is:", result)