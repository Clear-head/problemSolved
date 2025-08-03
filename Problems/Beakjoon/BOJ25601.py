from sys import stdin, exit

cast = {}

for _ in range(int(stdin.readline().rstrip()) - 1):
    a, b = map(str, stdin.readline().rstrip().split())
    cast[a] = b

a, b = map(str, stdin.readline().rstrip().split())

tmp1 = a
tmp2 = b


def func(target, source):
    f = cast.get(source, -1)
    if f == target:
        return True
    elif f == -1:
        return False
    else:
        return func(target, f)


print(1) if (func(a, tmp2) or func(b, tmp1)) else print(0)
