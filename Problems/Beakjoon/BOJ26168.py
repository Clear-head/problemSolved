"""

1 k: 배열 A의 원소 중 k보다 크거나 같은 원소의 개수를 출력한다.
2 k: 배열 A의 원소 중 k보다 큰 원소의 개수를 출력한다.
3 i j: 배열 A의 원소 중 i보다 크거나 같고 j보다 작거나 같은 원소의 개수를 출력한다.

    미완
\
"""

import sys
INF = sys.maxsize

def case1(k, lst):
    """
    @param k: tmp[1]
    @param lst: a
    @return: 배열 A의 원소 중 k보다 크거나 같은 원소의 개수를 출력한다.
    """
    start = 0
    end = len(lst) - 1
    ans = INF

    while start < end:
        mid = (start + end) // 2
        print(mid)

        if lst[mid] == k:
            ans = len(lst) - mid + 1

        elif lst[mid] > k:
            end = mid - 1

        else:
            start = mid + 1

    if ans != INF:
        return


def case2(k, lst):
    """
    @param k: tmp[1]
    @param lst: a
    @return: 배열 A의 원소 중 k보다 큰 원소의 개수를 출력한다.
    """
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == k:
            return len(lst) - mid

        elif lst[mid] > k:
            end = mid

        else:
            start = mid

    return 0


def case3(i, j, lst):
    """
    @param i: tmp[1]
    @param j: tmp[2]
    @param lst: a
    @return: 배열 A의 원소 중 i보다 크거나 같고 j보다 작거나 같은 원소의 개수를 출력한다.
    """
    left = 0
    right = 0

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == i:
            left = len(lst) - mid

        elif lst[mid] > i:
            end = mid - 1

        else:
            start = mid + 1

    start = left
    end = len(lst) - 1

    while start < end:
        mid = (start + end) // 2

        if lst[mid] == j:
            right = len(lst) - mid

        elif lst[mid] > j:
            end = mid - 1

        else:
            start = mid + 1

    return right - left


n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a = sorted(a)
print(a)

for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))

    if tmp[0] == 1:
        print(case1(tmp[1], a))

    elif tmp[0] == 2:
        print(case2(tmp[1], a))

    else:
        print(case3(tmp[1], tmp[2], a))
