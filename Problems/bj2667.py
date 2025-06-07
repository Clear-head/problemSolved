"""

    미완성

"""

from collections import deque
import sys

tc = int(sys.stdin.readline().rstrip())

box = deque()

for _ in range(tc):
    box.append(deque(list(map(int, sys.stdin.readline().rstrip().split("")))))


def sol(start, graph):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
