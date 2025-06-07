
"""

    완성

"""

import sys

n, hp, up = map(int, sys.stdin.readline().rstrip().split(" "))

# village = []
targets = []
home = set()

visited = set()
ans = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    for j in range(len(row)):
        if row[j] == 2:
            targets.append((i, j))

        elif row[j] == 1:
            home = (i, j)

    # village.append(row)


def cal_distance(r, s):
    return abs(r[0] - s[0]) + abs(r[1] - s[1])


def find(pos, now_hp, cnt):
    global ans
    global visited
    global home
    global targets

    if now_hp >= cal_distance(pos, home):
        ans = max(ans, cnt)

    for target in targets:
        if target in visited:
            continue
        if now_hp >= cal_distance(pos, target):
            visited.add(target)
            find(target, now_hp - cal_distance(pos, target) + up, cnt + 1)
            visited.discard(target)


find(home, hp, 0)
print(ans)
