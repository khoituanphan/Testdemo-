def zero_ending(scores):
    total = 0
    for num in scores:
        if num % 10 == 0:
            total += num
    return total
print(zero_ending([200, 456, 300, 100, 234, 678]))