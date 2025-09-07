coin_weight = [1, 2, 5, 7]

n = int(input())

dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = min([dp[i-j] for j in coin_weight if i >= j]) + 1

print(dp[n])
