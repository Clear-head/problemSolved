
"""

    완성

"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
card = list(map(int, sys.stdin.readline().rstrip().split(" ")))

card = sorted(card)

ans = 0

for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            if card[i] + card[j] + card[k] <= m:
                ans = max(ans, card[i] + card[j] + card[k])
            else:
                break

print(ans)