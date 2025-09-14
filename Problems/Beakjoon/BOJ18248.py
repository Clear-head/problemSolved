from sys import stdin, exit

n, m = map(int, stdin.readline().rstrip().split())
if n == 1 or m == 1:
    print("YES")
    exit()

listener = sorted([tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)])

for i in range(0, m-1):
    for j in range(1, m):
        if sorted(listener, key=lambda x:x[i]) != sorted(listener, key=lambda x:x[j]):
            print("NO")
            exit()

print("YES")
