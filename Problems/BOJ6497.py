import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1


while True:
    m, n = map(int, sys.stdin.readline().split())
    rank = [0] * (m + 1)

    if m == 0 and n == 0:
        break

    city = []
    parent = [i for i in range(m)]

    for _ in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        city.append((tmp[0], tmp[1], tmp[2]))

    city = sorted(city, key=lambda x: x[2])

    total_weight = 0
    weight = 0

    for a, b, c in city:
        total_weight += c
        if find(a) != find(b):
            union(a, b)
            weight += c

    print(total_weight - weight)
