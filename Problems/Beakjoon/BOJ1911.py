from sys import stdin

m, n = map(int, stdin.readline().split())
pool = []

for ___ in range(m):
    pool.append(list(map(int, stdin.readline().split())))
pool = sorted(pool)

cur_pos = 0

cnt = 0

for start, end in pool:
    if start > cur_pos:
        cur_pos = start

    tmp = end - cur_pos

    if tmp % n == 0:
        cnt += tmp // n
        cur_pos += tmp // n * n

    else:
        cnt += tmp // n + 1
        cur_pos += tmp // n * n + n


print(cnt)
