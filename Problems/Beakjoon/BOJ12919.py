from sys import stdin, exit

start = stdin.readline().rstrip()
target = stdin.readline().rstrip()

ans = 0


def recursion(string):
    if len(string) <= len(start):
        if string == start:
            print(1)
            exit()
        else:
            return

    if string[-1] == "A":
        recursion(string[:-1])

    if string[0] == "B":
        recursion(string[1:][::-1])


recursion(target)
print(0)
