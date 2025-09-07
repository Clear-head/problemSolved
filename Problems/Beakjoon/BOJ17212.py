coin_weight = [1, 2, 5, 7]

n = int(input())

dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    tmp = [dp[i-j] + 1 for j in coin_weight if i >= j]
    dp[i] = min(tmp)

print(dp[n])
