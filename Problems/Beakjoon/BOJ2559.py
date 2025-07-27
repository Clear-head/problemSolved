from sys import stdin

n, k = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

for i in range(1, n):
    nums[i] += nums[i - 1]

ans = nums[k-1]

for i in range(n-k):
    ans = max(ans, nums[k + i] - nums[i])

print(ans)

# ans = 0
# tmp = 0
#
# for i in range(k):
#     ans += nums[i]
#
# tmp = ans
# for i in range(n-k):
#     tmp += nums[i+k]-nums[i]
#     ans = max(ans, tmp)
#
# print(ans)
