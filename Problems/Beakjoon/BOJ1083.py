from sys import stdin

n = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().rstrip().split()))
cost = int(stdin.readline().rstrip())
ans = sorted(nums, reverse=True)

if n == 1 or cost == 0 or ans == nums:
    print(*nums)
    exit()


for i in range(n):
    max_num = i
    for j in range(i, min(i+cost+1, n)):
        if nums[j] > nums[max_num]:
            max_num = j

    cost -= max_num-i

    for ii in range(max_num, i, -1):
        nums[ii], nums[ii - 1] = nums[ii - 1], nums[ii]

    if cost == 0:
        break


print(*nums)
