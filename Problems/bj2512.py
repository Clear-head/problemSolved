import sys

n = int(sys.stdin.readline().rstrip())

hope_budget = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline().rstrip())

start = 1
end = max(hope_budget)
result_mid = None

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in hope_budget:
        if i > mid:
            result += mid
        else:
            result += i

    if result > budget:
        end = mid - 1

    elif result < budget:
        start = mid + 1
        result_mid = mid

    else:
        result_mid = mid
        break

print(result_mid)
