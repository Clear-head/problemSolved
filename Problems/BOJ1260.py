"""

    미완성

"""

import sys
from collections import deque



bfs_step = []
dfs_step = []


def bfs(start_node, graph):
    queue = deque([start_node])
    bfs_step.append(start_node)
    visited = set()
    visited.add(start_node)

    while queue:
        curr_node = queue.popleft()

        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
                bfs_step.append(next_node)
    return -1


def dfs(start_node, graph):
    queue = deque([start_node])
    dfs_step.append(start_node)
    visited = set()
    visited.add(start_node)

    while queue:
        curr_node = queue.pop()

        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
                dfs_step.append(next_node)
    return -1


graph = {}
n, m, v = map(int, sys.stdin.readline().rstrip().split())


for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if v == 1:
        print(b, a)
    if a not in graph:
        graph[a] = [b]
    elif a in graph:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    elif b in graph:
        graph[b].append(a)

# for i in graph.keys():
#     graph[i] = sorted(graph[i])

print(graph)
bfs(v, graph)
dfs(v, graph)

print(dfs_step)
print(bfs_step)
