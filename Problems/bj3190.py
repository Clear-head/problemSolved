"""

    완성
    1, 1 에는 사과 X -> 시작 지점
    X초가 끝나고 방향 전환

"""

import sys
from collections import deque


def direct(now, w):  # 1: 좌, 2: 하, 3: 우, 4:상
    if w == "D":
        if now == 1:
            return 4
        elif now == 2:
            return 1
        elif now == 3:
            return 2
        elif now == 4:
            return 3
    else:
        if now == 1:
            return 2
        elif now == 2:
            return 3
        elif now == 3:
            return 4
        else:
            return 1


def step():  # 1: 좌, 2: 하, 3: 우, 4:상
    next_step = [pos[0][0], pos[0][1]]

    if direction == 1:
        next_step[1] -= 1
    elif direction == 2:
        next_step[0] += 1
    elif direction == 3:
        next_step[1] += 1
    elif direction == 4:
        next_step[0] -= 1

    if next_step in pos:
        return True
    elif next_step[0] <= -1 or next_step[1] <= -1 or next_step[0] >= n or next_step[1] >= n:
        return True

    if next_step not in apple:
        pos.pop()
    else:
        apple.remove(next_step)

    pos.appendleft(next_step)

    return False


n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

apple = deque()

for _ in range(k):
    tt = list(map(int, sys.stdin.readline().rstrip().split()))
    apple.append([tt[0]-1, tt[1]-1])

move = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    move.append(list(map(str, sys.stdin.readline().rstrip().split())))

time = 0
pos = deque([[0, 0]])
direction = 3  # 1: 좌, 2: 하, 3: 우, 4:상

is_attack = False

tmp = move.popleft()

while True:

    time += 1

    if time != int(tmp[0]):
        is_attack = step()

    else:
        is_attack = step()
        direction = direct(direction, tmp[1])
        if move:
            tmp = move.popleft()
        else:
            tmp = [-1, -1]

    if is_attack:
        print(time)
        break
