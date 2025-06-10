"""

    미완성

"""
from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    m, n, k = map(int, sys.stdin.readline().rstrip().split(" "))
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    y = a
    x = b
    for ii in range(k - 1):
        a, b = map(int, sys.stdin.readline().rstrip().split(" "))
        field[b][a] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque((x, y))
    visited = set((nx, ny))
    area_cnt = 1

    while queue:
        x, y = queue.popleft()

        flag = True

        for iii in range(4):
            nx = x + dx[iii]
            ny = y + dy[iii]

            if 0 <= x < len(field) and 0 <= y < len(field[0]):
                if not (nx, ny) in visited:
                    visited.add((nx, ny))

                    if field[x][y] == 0 and field[nx][ny] == 1:
                        area_cnt += 1
