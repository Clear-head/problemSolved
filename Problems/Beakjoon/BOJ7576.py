"""

    미완성

"""

import sys
from collections import deque

dic = {}
dic.keys()

m, n = map(int, sys.stdin.readline().rstrip().split(" "))
box = []
day = 1
zero_count = 0
start_dq = deque()
dq = deque()
what = True

for i in range(n):
    box.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            start_dq.append((i, j))
        elif box[i][j] == 0:
            zero_count += 1

if zero_count == 0:
    print(0)
    sys.exit()

start_cnt = len(start_dq)
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
flag = True
visited = set(start_dq)
print(zero_count)

while what:
    print()
    print()
    print()

    for i in range(n):
        print(box[i])

    x, y = start_dq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(box) and 0 <= ny < len(box[0]):
            if (nx, ny) not in visited:

                visited.add((nx, ny))

                if box[x][y] == 1 and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    zero_count -= 1

                if len(visited) == m * n:
                    what = False
                    break

                dq.append((nx, ny))

    if not start_dq:
        day += 1
        for i in range(len(dq)):
            start_dq.append(dq.pop())
        dq.clear()

if zero_count > 0:
    print(-1)
else:
    print(day)
