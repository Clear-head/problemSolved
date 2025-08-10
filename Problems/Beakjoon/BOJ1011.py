from sys import stdin
from math import sqrt


def sol(x, y):
    dist = y - x
    n = int(sqrt(dist))

    if n**2 == dist:
        return 2*n - 1
    elif n**2 + n >= dist:
        return 2 * n
    else:
        return 2*n + 1


for _ in range(int(stdin.readline().rstrip())):
    print(sol(*map(int, stdin.readline().split())))
