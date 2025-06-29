import sys

n, x = map(int, sys.stdin.readline().split())

layer = [1] * (n+1)
patty = [1] * (n+1)

for i in range(1, n+1):
    layer[i] = 2 * layer[i - 1] + 3
    patty[i] = 2 * patty[i - 1] + 1


def recursive(lv, wanna):

    if lv == 0:
        return 1 if wanna >= 1 else 0

    total_layer = layer[lv]
    mid = layer[lv - 1] + 2

    if wanna == 1:
        return 0

    elif wanna <= 1 + layer[lv-1]:
        return recursive(lv-1, wanna-1)

    elif wanna == mid:
        return recursive(lv-1, wanna-1) + 1

    elif wanna < total_layer:
        return recursive(lv-1, wanna-1) + recursive(lv-1, wanna - mid) + 1

    else:
        return patty[lv]


print(recursive(n, x))
