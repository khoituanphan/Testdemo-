pascal_triangle_row = []
def pascal_triag(n):
    if n == 0:
        return []
    elif n == 1:
        pascal_triangle_row.append([1])
        return [1]
    else:
        new_row = [1]
        previous_row = pascal_triag(n-1)
        for i in range(len(previous_row)-1):
            new_row.append(previous_row[i] + previous_row[i+1])
        new_row += [1]
        pascal_triangle_row.append(new_row)
    return new_row

n = 10
pascal_triag(n)

for i in range(0, n):
    sum = 0
    for j in range(0, i + 1):
        if j <= i - j:
            sum += pascal_triangle_row[i - j][j]
    print(sum)
