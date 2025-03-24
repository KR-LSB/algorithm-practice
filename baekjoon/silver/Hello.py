t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    floor = [i for i in range(1, n + 1)]

    for j in range(1, k + 1):
        for l in range(1, n):
            floor[l] += floor[l - 1]
    print(floor[n - 1])