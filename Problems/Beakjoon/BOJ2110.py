import sys

n, c = map(int, sys.stdin.readline().split())

home = [int(sys.stdin.readline().rstrip()) for i in range(n)]

home = sorted(home)

ans = 0
start = 1
end = home[-1] - home[0]

while start <= end:

    mid = (start + end) // 2
    cnt = 1
    tmp = home[0]

    for i in range(1, n):
        if home[i] >= mid + tmp:
            tmp = home[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        ans = mid

    else:
        end = mid - 1

print(ans)
