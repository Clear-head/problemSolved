"""

    완료

"""

import sys

mv = 0.0000001


def living_empty(lst, l, r):
    for ii in range(len(lst)):

        if lst[ii][0] <= l <= lst[ii][1] <= r:
            lst[ii][1] = l

        elif l <= lst[ii][0] <= r <= lst[ii][1]:
            lst[ii][0] = l

        elif l <= lst[ii][0] <= lst[ii][1] <= r:
            lst.pop(ii)

        elif lst[ii][0] <= l < r <= lst[ii][1]:
            lst.pop(ii)
            lst.append([lst[ii][0] + mv, l - mv])
            lst.append([r + mv, lst[ii][1] - mv])

    return lst


def solution(lst, ww):
    start = 0.0
    end = 0.0
    empty = []

    for i in range(len(lst)):

        left = lst[i] - ww / 2 if lst[i] - ww / 2 >= 0 else 0.0
        right = lst[i] + ww / 2

        if left <= start <= right <= end:
            start = left

        elif start <= left <= end <= right:
            end = right

        elif end < left:
            empty.append([end + mv, left - mv])

        elif left <= start < end <= right:
            end = right
            start = left

            if empty:
                empty = living_empty(empty, left, right)

    return end - start


nx, ny, w = 1, 1, 1.0

while True:

    nx, ny, w = map(float, sys.stdin.readline().rstrip().split(" "))

    if nx == 0 == ny and w == 0.0:
        break

    width = sorted(list(map(float, sys.stdin.readline().rstrip().split(" "))))
    length = sorted(list(map(float, sys.stdin.readline().rstrip().split(" "))))

    if solution(width, w) >= 75 and solution(length, w) >= 100:
        print("YES")
    else:
        print("NO")
