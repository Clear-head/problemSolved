import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

if n == 2:
    print(1)
    sys.exit()
elif n == 1:
    print(0)
    sys.exit()

num = deque()
num.append(int(sys.stdin.readline().rstrip()))


ans = 0
for i in range(n - 1):

    tmp = int(sys.stdin.readline().rstrip())

    if len(num) == 1:
        num.append(tmp)
        continue

    if tmp < num[-1]:
        cnt = 0
        while len(num) > 1:
            cnt += 1
            num.popleft()
        ans += sum([i for i in range(1, cnt + 1)])
        print(f"ans: {ans}")

    elif tmp > num[-1]:
        cnt = 0
        while len(num) > 1:
            cnt += 1
            num.pop()
        ans += sum([ 1 + i for i in range(1, cnt+1)])
        print(f"ans: {ans}")


    num.append(tmp)

if len(num) == 2:
    ans += 1
else:
    if num[0] < num[-1]:
        ans += sum([i for i in range(1, len(num) - 2)])
    else:
        ans += sum([i for i in range(1, len(num) - 1)])

print(num)
print(ans)
