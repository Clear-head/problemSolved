from sys import stdin

cs = {}
ans = 0

for _ in range(int(stdin.readline())):
    c, s = map(str, stdin.readline().rstrip().split())
    c = c[:2]

    if c == s:
        continue

    k = (c, s)

    if cs.get(k):
        cs[k] += 1
    else:
        cs[k] = 1

for i in cs.keys():

    rev = (i[1], i[0])
    if cs.get(rev):
        ans += cs.get(rev) * cs.get(i)

print(ans//2)

