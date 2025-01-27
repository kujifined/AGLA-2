def gaussian_elimination(matrix):
    matrix = [row.copy() for row in matrix]
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    variables = cols - 1
    for i in range(min(rows, variables)):
        for pivot_row in range(i, rows):
            if matrix[pivot_row][i] != 0:
                break
        else:
            continue
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
        pivot = matrix[i][i]
        for j in range(i + 1, rows):
            factor = matrix[j][i] / pivot
            for k in range(i, cols):
                matrix[j][k] -= factor * matrix[i][k]
    for row in matrix:
        if all(abs(x) < 1e-8 for x in row[:-1]) and abs(row[-1]) > 1e-8:
            return "No solutions"
    solution = [0.0] * variables
    for i in range(variables - 1, -1, -1):
        if i >= rows:
            solution[i] = 0.0
            continue
        row = matrix[i]
        sum_val = sum(row[j] * solution[j] for j in range(i + 1, variables))
        if abs(row[i]) < 1e-8:
            if abs(row[-1] - sum_val) < 1e-8:
                solution[i] = 0.0
            else:
                return "No solutions"
        else:
            solution[i] = (row[-1] - sum_val) / row[i]
    return [round(x, 4) for x in solution]
matrix = [
    [1, 1, 1, 6],
    [2, 1, 3, 14],
    [3, 4, 1, 13],
    [1, -1, 2, 7]
]
print("Solution: ")
for i in gaussian_elimination(matrix):
    print(i)
