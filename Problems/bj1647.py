import sys

"""

    완성
    객체지향화 하려면 함수에 변수를 추가, 클래스 만들기

"""

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    find_a = find(x)
    find_b = find(y)

    if find_a < find_b:
        parent[find_b] = find_a
    else:
        parent[find_a] = find_b


N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N + 1)]
edges = []
max_weight = -1
total_weight = 0

for _ in range(M):
    j, k, l = map(int, sys.stdin.readline().split())
    edges.append((j, k, l))

edges = sorted(edges, key=lambda x: x[2])

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        total_weight += c
        max_weight = max(max_weight, c)

print(total_weight - max_weight)
