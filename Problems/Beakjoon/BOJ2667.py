"""

    미완성

"""

from collections import deque
import sys

DX = [0, 0, 1, -1]
DY = [-1, 1, 0, 0]

n = int(sys.stdin.readline().rstrip())

box = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
complex = []

visited = set()

def sol(start):
    q = deque()
    q.append(start)
    visited.add(start)
    cnt = 1

    while q:
        (x, y) = q.popleft()

        for i in range(4):
            nx = x + DX[i]
            ny = y + DY[i]

            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) not in visited and box[nx][ny] != 0:
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        print(visited)
        if box[i][j] not in visited and box[i][j] != 0:
            complex.append(sol((i, j)))


# complex = list(set(complex))
print(len(complex))
for i in sorted(complex):
    print(i)
