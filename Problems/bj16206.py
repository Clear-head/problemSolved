
"""

    완성

"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
cake = list(map(int, sys.stdin.readline().rstrip().split(" ")))

cnt = 0
tmp = []

for i in range(n):
    if cake[i] == 10:
        cnt += 1
        tmp.append(cake[i])
    elif cake[i] < 10:
        tmp.append(cake[i])


for i in tmp:
    cake.remove(i)

cake_length = len(cake)
cake = sorted(cake, key=lambda x: (x % 10, x))

for i in range(cake_length):
    while cake[i] >= 10 and m > 0:
        if cake[i] > 10:
            cnt += 1
            cake[i] -= 10
            m -= 1
        if cake[i] == 10:
            cnt += 1
            break
print(cnt)
