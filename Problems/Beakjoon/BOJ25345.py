from math import comb
n, k = map(int, input().split())
print((comb(n, k) * (2 ** (k-1))) % (10**9 + 7))
