"""

    완성

"""

from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

dq = []
for _ in range(n):
    dq.append(list(map(int, sys.stdin.readline().rstrip().split())))

dq = deque(sorted(dq, key=lambda x: (x[0], x[1])))

i = 0
tmp = dq.popleft()
cnt = 1
start = tmp[0]
end = tmp[1]

while dq:
    tmp = dq.popleft()
    if start <= tmp[0] < end and tmp[1] < end:
        start = tmp[0]
        end = tmp[1]
    elif end <= tmp[0]:
        end = tmp[1]
        cnt += 1
print(cnt)
