
"""

    미완성

"""

import sys

n = int(sys.stdin.readline().rstrip())
number = []
ans = 0
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    for j in range(len(row)):
        if row[j] != 0:
            number.append((i, j, row[j]))
# print(number)


def make(stat):
    mm = [[0] * n for _ in range(n)]
    print(len(mm))
    print(len(mm[0]))

    for i in stat:
        mm[i[0]][i[1]] = i[2]
    for i in mm:
        print(i)
    print("\n\n")


def move(can_move, stat):
    global ans
    make(stat)
    for num in stat:
        ans = max(num[2], ans)
    if can_move == 0 or len(stat) < 2:
        return

    up(can_move, stat)
    down(can_move, stat)
    left(can_move, stat)
    right(can_move, stat)


def up(can_move, stat):
    stat = sorted(stat, key=lambda x: (x[1], x[0]))
    next = []
    visited = []

    tmp = 0
    for i in range(len(stat) - 1):

        if stat[i] in visited:
            continue

        if len(next) > 0 and next[-1][0] == stat[i][0]:
            tmp = next[-1][1] + 1

        if stat[i][2] == stat[i + 1][2] and stat[i][0] == stat[i + 1][0]:
            next.append((stat[i][0], tmp, stat[i][2] * 2))
            visited.append(stat[i])
            visited.append(stat[i + 1])
        else:
            next.append((stat[i][0], tmp, stat[i][2]))
            visited.append(stat[i])

        tmp = 0

    for t in stat:
        if t not in visited:
            if len(next) > 0 and t[0] == next[-1][0]:
                tmp = next[-1][1] + 1
            next.append((t[0], tmp, t[2]))

    move(can_move - 1, next)


def down(can_move, stat):
    stat = sorted(stat, key=lambda x: (-x[1], x[0]))

    visited = []
    next = []

    tmp = n - 1
    for i in range(len(stat) - 1):

        if stat[i] in visited:
            continue

        if len(next) > 0 and next[-1][0] == stat[i][0]:
            tmp = next[-1][1] - 1

        if stat[i][2] == stat[i + 1][2] and stat[i][0] == stat[i + 1][0]:
            next.append((stat[i][0], tmp, stat[i][2] * 2))
            visited.append(stat[i])
            visited.append(stat[i + 1])
        else:
            next.append((stat[i][0], tmp, stat[i][2]))
            visited.append(stat[i])

        tmp = n - 1

    for t in stat:
        if t not in visited:
            if len(next) > 0 and t[0] == next[-1][0]:
                tmp = next[-1][1] - 1
            next.append((t[0], tmp, t[2]))

    move(can_move - 1, next)


def left(can_move, stat):
    stat = sorted(stat, key=lambda x: (x[0], x[1]))
    next = []
    visited = []

    tmp = 0

    for i in range(len(stat) - 1):
        if stat[i] in visited:
            continue

        if len(next) > 0 and stat[i][1] == next[-1][1]:
            tmp = next[-1][0] + 1

        if stat[i][2] == stat[i + 1][2] and stat[i][1] == stat[i + 1][1]:
            next.append((tmp, stat[i][1], stat[i][2] * 2))
            visited.append(stat[i])
            visited.append(stat[i + 1])
        else:
            next.append((tmp, stat[i][1], stat[i][2]))
            visited.append(stat[i])

        tmp = 0

    for t in stat:
        if t not in visited:
            if len(next) > 0 and t[1] == next[-1][1]:
                tmp = next[-1][0] + 1
            next.append((tmp, t[1], t[2]))

    move(can_move - 1, next)


def right(can_move, stat):
    stat = sorted(stat, key=lambda x: (-x[0], x[1]))
    next = []
    visited = []

    tmp = n - 1

    for i in range(len(stat) - 1):
        if stat[i] in visited:
            continue
        if len(next) > 0 and stat[i][1] == next[-1][1]:
            tmp = next[-1][0] - 1

        if stat[i][2] == stat[i + 1][2] and stat[i][1] == stat[i + 1][1]:
            next.append((tmp, stat[i][1], stat[i][2] * 2))
            visited.append(stat[i])
            visited.append(stat[i + 1])
        else:
            next.append((tmp, stat[i][1], stat[i][2]))
            visited.append(stat[i])

        tmp = n - 1

    for t in stat:
        if t not in visited:
            if len(next) > 0 and t[1] == next[-1][1]:
                tmp = next[-1][0] - 1
            next.append((tmp, t[1], t[2]))

    move(can_move - 1, next)


move(5, number)

print(ans)
