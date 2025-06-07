"""

    완성

"""

from collections import deque
import sys

visited = set()
cnt = 0


def bfs(x, y, area, color):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()

    visited.add((x, y))
    q.append((x, y))

    while q:
        x, y = q.pop()

        for iii in range(4):
            nx = x + dx[iii]
            ny = y + dy[iii]
            if 0 <= nx < len(area) and 0 <= ny < len(area[0]):
                if (nx, ny) not in visited and area[nx][ny] == color:
                    q.append((nx, ny))
                    visited.add((nx, ny))


graph = []
graph_no_green = []
n = int(input().rstrip())
for _ in range(n):
    tmp = list(map(str, sys.stdin.readline().rstrip()))
    temp = []
    graph.append(tmp)
    for iv in tmp:
        if iv == 'G':
            temp.append('R')
        else:
            temp.append(iv)
    graph_no_green.append(temp)

for i in range(n):
    for ii in range(n):
        if (i, ii) not in visited:
            bfs(i, ii, graph, graph[i][ii])
            cnt += 1

print(cnt)

#   적록색약 인 사람
visited.clear()
cnt = 0

for i in range(n):
    for ii in range(n):
        if (i, ii) not in visited:
            bfs(i, ii, graph_no_green, graph_no_green[i][ii])
            cnt += 1
print(*asd)
print(cnt)

