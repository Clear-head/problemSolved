from sys import stdin
from collections import Counter

n = int(stdin.readline())
dots = []
x_dic = []
y_dic = []
cnt = 0

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    x_dic.append(a)
    y_dic.append(b)
    dots.append((a, b))

x_dic = Counter(x_dic)
y_dic = Counter(y_dic)

for dot in dots:
    cnt += (x_dic.get(dot[0], 0)-1) * (y_dic.get(dot[1], 0)-1)

print(cnt)