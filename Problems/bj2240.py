
"""

    미완성

"""

import sys

"""

    1. 위치가 같고 받을 때
    2. 위치가 다르고 받을때
    3. 위치가 다르고 받지 않을때
    
"""

t, w = map(int, sys.stdin.readline().rstrip().split(" "))

# 0 = catch, 1 = no catch
dp = [[[0 for _ in range(2)] for _ in range(31)] for _ in range(1001)]

print(len(dp))
print(len(dp[0]))
print(len(dp[0][0]))

cnt = w
pos = 0

for i in range(1, t+1):
    plum_pos = int(sys.stdin.readline().rstrip()) - 1
    if cnt > 0:
        if 1 == plum_pos:
            dp[i][cnt][pos] = max(dp[i-1][cnt][1], dp[i-1][cnt][0]) + 1
            dp[i][cnt][pos] = max(dp[i - 1][cnt][1], dp[i - 1][cnt][0])

        else:
            dp[i][cnt][pos] = max(dp[i - 1][cnt][1], dp[i - 1][cnt][0]) + 1
            dp[i][cnt][pos] = max(dp[i - 1][cnt][1], dp[i - 1][cnt][0])



