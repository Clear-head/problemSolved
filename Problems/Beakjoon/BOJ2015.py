from sys import stdin

ans = 0
n, k = map(int, stdin.readline().rstrip().split())
nums = {0:1}

prefix_sum = 0

for i in list(map(int, stdin.readline().rstrip().split())):
    prefix_sum += i
    ans += nums.get(prefix_sum - k, 0)
    nums[prefix_sum] = nums.get(prefix_sum, 0) + 1


print(ans)
