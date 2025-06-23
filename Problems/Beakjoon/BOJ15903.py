import sys
import heapq


n, m = map(int, sys.stdin.readline().split())
heap = list(map(int, sys.stdin.readline().split()))

heapq.heapify(heap)

for _ in range(m):
    tmp = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, tmp)
    heapq.heappush(heap, tmp)

print(sum(heap))