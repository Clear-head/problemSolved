from sys import stdin

n, b, a = map(int, stdin.readline().split())
cost = sorted(list(map(int, stdin.readline().split())))

prefix = [0 for _ in range(n+1)]

cnt = 0

for i in range(n):
    prefix[i + 1] = prefix[i] + cost[i]

for i in range(1, n+1):
    non_sale = prefix[i - min(a, i)]
    total = non_sale + (prefix[i] - non_sale)//2

    if total <= b:
        cnt = i
    else:
        break


print(cnt)
