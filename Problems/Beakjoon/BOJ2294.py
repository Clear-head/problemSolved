"""

    미완성

"""

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

coin = []
dp = deque([[0]])

for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a <= k:
        coin.append(a)

if len(coin) == 0:
    print(-1)
    sys.exit()

elif len(coin) == 1 and k % coin[0] != 0:
    print(-1)
    sys.exit()

print(coin)
