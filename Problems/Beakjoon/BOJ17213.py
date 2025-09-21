from math import comb

n = int(input())
m = int(input())

print(comb(m-1, m-n))