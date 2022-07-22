def pascal2(n):
    if n == 0:
        return []
    elif n == 1:
        print([1])
        return [1]
    else:
        pascal_triangle = [1]
        new_line = pascal2(n - 1)
        for i in range(len(new_line) - 1):
            pascal_triangle.append(new_line[i] + new_line[i + 1])
        pascal_triangle += [1]
        print(pascal_triangle)
    return pascal_triangle
pascal2(6)