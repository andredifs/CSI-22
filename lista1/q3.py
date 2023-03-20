def sum_to(n):
    res = 0

    for i in range(n+1):
        res += i

    return res

print(sum_to(10))