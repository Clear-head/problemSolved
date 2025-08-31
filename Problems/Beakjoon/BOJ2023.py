from math import isqrt

n = int(input())

start_number = [2, 3, 5, 7]
last_number = [1, 3, 7, 9]


def is_prime(num):
    for i in range(2, isqrt(num)):
        if num % i == 0:
            return False
    return True


def recursive(num, limit, cnt):

    if cnt == limit:
        print(num)
        return

    num *= 10

    for i in last_number:
        if is_prime(num+i):
            recursive(num+i, limit, cnt+1)

    return


for a in start_number:
    recursive(a, n, 1)

