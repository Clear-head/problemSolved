"""

    완성

"""

import sys
import heapq

INF = sys.maxsize

n, e = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
distance = [[INF] * (n + 1) for _ in range(3)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = graph[b][a] = c

v1, v2 = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] <= dist:
            continue

        distance[now] = dist

        for i in range(1, n + 1):
            if graph[now][i] != INF:
                heapq.heappush(q, (graph[now][i] + dist, i))


dijkstra(1, distance[0])
dijkstra(v1, distance[1])
dijkstra(v2, distance[2])
print(distance[0])
print(distance[1])
print(distance[2])

route1 = distance[0][v1] + distance[1][v2] + distance[2][n]
route2 = distance[0][v2] + distance[2][v1] + distance[1][n]
tmp = min(route1, route2)

if tmp >= INF:
    print(-1)
else:
    print(tmp)
