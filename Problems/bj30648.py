
"""

    완성

"""

import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
r = int(sys.stdin.readline().rstrip())
cnt = 0
flower = [[a, b]]

while True:
    cnt += 1

    if a + b + 2 < r:
        if [a + 1, b + 1] not in flower:
            flower.append([a+1, b+1])
            a += 1
            b += 1
        else:
            print(cnt)
            break
    else:
        if [a // 2, b // 2] not in flower:
            flower.append([a // 2, b // 2])
            a //= 2
            b //= 2
        else:
            print(cnt)
            break
