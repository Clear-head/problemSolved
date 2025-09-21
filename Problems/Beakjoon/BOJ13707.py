from math import comb
a, b = map(int, input().split())
print(comb(a+b-1, b-1)%1000000000)
