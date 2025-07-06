from sys import stdin
from collections import deque


def recursive(num, made):
    if not num:

        if eval(made.replace(" ", "")) == 0:
            temp.append(made)
        return

    num = deque(num)
    tmp = num.popleft()

    recursive(num, made + "+" + tmp)
    recursive(num, made + "-" + tmp)
    recursive(num, made + " " + tmp)


T = int(stdin.readline().rstrip())
ans = []
for _ in range(T):
    temp = []
    nums = deque([str(i) for i in range(1, int(stdin.readline().rstrip())+1)])

    recursive(nums, nums.popleft())

    ans.extend(sorted(temp))
    ans.append('')

for i in ans:
    print(i)

