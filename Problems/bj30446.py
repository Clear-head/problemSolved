
"""

    해야함

"""

from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

if n < 10:
    print(n)
    sys.exit()
elif n == 10:
    print(9)
    sys.exit()

cnt = 9
k = 11

if n > 10 ** 9:
    cnt = 109998
    k = 10 ** 9 + 1
elif n > 10 ** 8:
    cnt = 19998
    k = 10 ** 8 + 1
elif n > 10 ** 7:
    cnt = 10998
    k = 10 ** 7 + 1
elif n > 10 ** 6:
    cnt = 1998
    k = 10 ** 6 + 1
elif n > 10 ** 5:
    cnt = 1098
    k = 10 ** 5 + 1
elif n > 10 ** 4:
    cnt = 198
    k = 10 ** 4 + 1
elif n > 10 ** 3:
    cnt = 108
    k = 10 ** 3 + 1
elif n > 100:
    cnt = 18
    k = 101
elif n > 10:
    cnt = 9
    k = 10

dic = {}

for i in range(k, n + 1):

    flag = True
    string = str(i)

    for j in range(len(string)):
        dic[j] = string[j]

    for j in range(len(string)//2):
        if dic[j] != dic[len(string) - j - 1]:
            flag = False
            break
    if flag:
        cnt += 1


print(cnt)
