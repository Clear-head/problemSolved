import sys


def find(p, x):
    if p[x] != x:
        p[x] = find(p, parent[x])
    return p[x]


def union(p, x, y):
    find_a = find(p, x)
    find_b = find(p, y)

    if find_a < find_b:
        p[find_b] = find_a
    else:
        p[find_a] = find_b

    return p


N, M = map(int, sys.stdin.readline().split())

gender = list(map(str, sys.stdin.readline().rstrip().split()))

parent = [i for i in range(N+1)]
edges = []
weight = 0
cnt = 0


for i in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    if gender[u-1] != gender[v-1]:
        edges.append((u, v, d))

edges = sorted(edges, key=lambda x: x[2])

for a, b, c in edges:
    if find(parent, a) != find(parent, b):
        parent = union(parent, a, b)
        weight += c
        cnt += 1


if cnt != N-1:
    print(-1)
else:
    print(weight)
