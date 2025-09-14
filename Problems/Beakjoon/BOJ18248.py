from sys import stdin, exit

n, m = map(int, stdin.readline().rstrip().split())
if n == 1 or m == 1:
    print("YES")
    exit()

listener = sorted([tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)])

ans = [sorted(listener, key=lambda x:x[i]) for i in range(m)]

for i in range(m-1):
    for j in range(1, m):
        if ans[i] != ans[j]:
            print("NO")
            exit()


print("YES")
