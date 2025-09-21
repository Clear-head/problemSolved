from math import comb
from sys import stdin

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

print(comb(m-1, m-n))