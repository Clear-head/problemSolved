import sys
import heapq

T = int(sys.stdin.readline())


while T > 0:
    T -= 1

    k = int(sys.stdin.readline())
    heap = list(map(int, sys.stdin.readline().split()))

    heapq.heapify(heap)
    cost = 0
    while True:
        if len(heap) == 1:
            break
        tmp = heapq.heappop(heap) + heapq.heappop(heap)
        cost += tmp
        heapq.heappush(heap, tmp)

    print("ans = ", heapq.heappop(heap))