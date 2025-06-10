"""

    완성

"""

import sys
from collections import deque

visited = set()
DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

n, m = map(int, sys.stdin.readline().split())

area = []

for _ in range(m):
    area.append(list(map(str, sys.stdin.readline().rstrip())))


def bfs(color, start_node):
    q = deque()
    q.append(start_node)
    visited.add(start_node)

    cnt = 1

    while q:
        x, y = q.popleft()

        if area[x][y] == color:
            for k in range(4):
                nx = x + DX[k]
                ny = y + DY[k]
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited and area[nx][ny] == color:
                        visited.add((nx, ny))
                        q.append((nx, ny))
                        cnt += 1

    return cnt * cnt


blue = 0
white = 0

for i in range(m):
    for ii in range(n):

        if (i, ii) not in visited:

            if area[i][ii] == "W":
                white += bfs("W", (i, ii))
            else:
                blue += bfs("B", (i, ii))

print(white, blue)
