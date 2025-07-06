import heapq, sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

score = 0
time = 24 * n

heap = []

for i, j in zip(a, b):
    if i == 100:
        score += 100
        continue
    heapq.heappush(heap, (-j, -i))

while time > 0 and heap:
    default = heapq.heappop(heap)
    time_per_sc = -default[0]
    de_sc = -default[1]

    used_time = (100 - de_sc) // time_per_sc

    if time < used_time:
        used_time = time

    time -= used_time
    now_score = (used_time * time_per_sc) + de_sc

    if now_score < 100:
        heapq.heappush(heap, (-(100 - now_score), -now_score))
    else:
        score += 100

while heap:
    score -= heapq.heappop(heap)[1]

print(score)
