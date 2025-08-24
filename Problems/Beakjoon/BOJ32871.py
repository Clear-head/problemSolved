from sys import stdin

t = int(stdin.readline().rstrip())

for ___ in range(t):
    n, m = map(int, stdin.readline().rstrip().split())
    if n == 1 or m == 1:
        print("YES")

    elif abs(n - m) % 2 != 0:
        print("YES")

    else:
        print("NO")
