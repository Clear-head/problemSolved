from sys import stdin
from re import findall

n = int(stdin.readline().rstrip())
serial = [stdin.readline().rstrip() for _ in range(n)]


def is_2(x):
    return sum(map(int, findall(r'\d', x)))


for i in sorted(serial, key=lambda x: (len(x), is_2(x), x)):
    print(i)
