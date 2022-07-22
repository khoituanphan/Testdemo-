
file1  = [[12, 7, 3],[4, 5, 6],[7, 8, 9]]
file2  = [[5, 8, 1],[6, 7, 3],[4, 5, 9]]
result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(len(file1)):
    for j in range(len(file1[0])):
        result[i][j] = file1[i][j] + file2[i][j]
for row in result:
    print(row)
