
"""

    완성

"""

import sys
from math import lcm

tc = int(sys.stdin.readline().rstrip())


def sol(lc, M, N, X, Y):

    if M == X:
        X = 0
    elif N == Y:
        Y = 0

    for ii in range(X, lc+1, M):
        if ii % N == Y and ii % M == X:
            return ii
    return -1


for t in range(tc):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    ll = lcm(m, n)

    if m == n and x != y:
        print(-1)
        continue
    elif m == x and n == y:
        print(ll)
        continue

    print(sol(ll, m, n, x, y))
