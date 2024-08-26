def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(4, 4, 11)
result2 = get_matrix(2, 2, 77)
result3 = get_matrix(6, 2, 13)
print(result1)
print(result2)
print(result3)
