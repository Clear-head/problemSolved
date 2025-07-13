import sys

N = int(sys.stdin.readline())
if N in [0, 1]:
    print(N)
    sys.exit()

q = [1 for i in range(N)]
visited = set()


def recursive(n, ex, target):
    if n == 0:
        print(" ".join(map(str, ex)))
        return
    for i in range(min(target, n), 0, -1):
        ex.append(i)
        recursive(n-i, ex, i)
        ex.pop()


recursive(N, [], N)
