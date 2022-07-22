def is_prime(x):
    for num in range(2, x):
        if x % num == 0:
            return False
    return True
for num in range(2, 200):
    if is_prime(num):
        print(num, end=" ")