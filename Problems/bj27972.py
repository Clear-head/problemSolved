"""

    미완성

"""

import sys

t = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split(" ")))

tmp = [-1 for _ in range(t)]

min_idx = a.index(min(a))
tmp[min_idx] = 1

if min_idx == len(a) - 1:

    for i in range(len(a) - 1, 0, -1):
        if a[i] == a[i - 1]:
            tmp[i - 1] = tmp[i]
        elif a[i] < a[i - 1]:
            tmp[i - 1] = tmp[i] + 1
        else:
            tmp[i - 1] = tmp[i] - 1

elif min_idx == 0:

    for i in range(1, len(a)):
        if a[i - 1] == a[i]:
            tmp[i] = tmp[i - 1]
        elif a[i - 1] > a[i]:
            tmp[i] = tmp[i - 1] - 1
        else:
            tmp[i] = tmp[i - 1] + 1

else:

    for i in range(min_idx, 0, -1):
        if a[i] == a[i - 1]:
            tmp[i - 1] = tmp[i]
        elif a[i] < a[i - 1]:
            tmp[i - 1] = tmp[i] + 1
        else:
            tmp[i - 1] = tmp[i] - 1

    for i in range(min_idx + 1, len(a)):
        if a[i - 1] == a[i]:
            tmp[i] = tmp[i - 1]
        elif a[i - 1] > a[i]:
            tmp[i] = tmp[i - 1] - 1
        else:
            tmp[i] = tmp[i - 1] + 1

print(tmp)
if min(tmp) < 1:
    print(max(tmp) + (1 - min(tmp)))

elif min(tmp) > 1:
    print(max(tmp) - (min(tmp) - 1))

else:
    print(max(tmp))
