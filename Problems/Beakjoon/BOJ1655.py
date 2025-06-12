from collections import deque
import heapq
from sys import stdin

n = int(stdin.readline().rstrip())

heap = []

for i in range(n):
    heapq.heappush(heap, int(stdin.readline().rstrip()))
    print(heap)
