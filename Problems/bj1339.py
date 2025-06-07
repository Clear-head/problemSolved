
"""

    완성

"""

import sys
from collections import deque

number = deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
alpha = {}

num = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    num.append(list(map(str, sys.stdin.readline().rstrip())))

dic = {}

m_tt = 0
st = ""

for i in num:
    m_tt = max(m_tt, len(i))
    for ii in i:
        st += ii

for i in set(st):
    alpha[i] = 0

for _ in range(len(number) - len(st)):
    number.pop()

for i in range(len(num)):
    if len(num[i]) < m_tt:
        for _ in range(m_tt - len(num[i])):
            num[i].insert(0, "-")

for i in num:
    for ii in range(len(i)):
        if i[ii] != "-":
            alpha[i[ii]] += 10**(len(set(st))-ii)

k = sorted(alpha.keys(), key=lambda x: -alpha[x])
for i in k:
    dic[i] = number.popleft()

ans = 0
for i in num:
    tmp = len(i)
    for ii in i:
        if ii != "-":
            ans += dic[ii] * (10 ** (tmp - 1))
        tmp -= 1

print(ans)
