from sys import stdin

n, m, k = map(int, stdin.readline().rstrip().split())
ans = 0

score = sorted([tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)], key=lambda x: x[1])

for _ in range(k):
    ans += score.pop()[0]

score = sorted(score, key=lambda x:x[0])

for _ in range(m):
    ans += score.pop()[0]

print(ans)
