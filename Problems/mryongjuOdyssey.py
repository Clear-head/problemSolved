import sys
import heapq

INF = sys.maxsize

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
distance = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
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


tmp = INF
dijkstra(v1, distance[v2])

for i in distance[v2]:
    if i != 0:
        tmp = min(tmp, i)
print(distance)
print(tmp)
