from sys import stdin
from collections import deque


T = int(stdin.readline().rstrip())


for ___ in range(T):
    n = int(stdin.readline().rstrip())
    nums = sorted(list(map(int, stdin.readline().split())))
    q1 = deque()
    flag = True

    while nums:
        if flag:
            q1.appendleft(nums.pop())
        else:
            q1.append(nums.pop())

        flag = not flag

    max1 = abs(q1[0] - q1[-1])
    tmp = q1.pop()
    while q1:
        tmp2 = q1.pop()
        max1 = max(max1, abs(tmp - tmp2))
        tmp = tmp2

    print(max1)

