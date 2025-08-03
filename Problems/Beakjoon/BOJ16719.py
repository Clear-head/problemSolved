from sys import stdin

target = list(stdin.readline().rstrip())
visited = [False for _ in range(len(target))]


def recursion():
    if all(visited):
        return

    tmp = "z"
    tmp_idx = -1

    for i in range(len(target)):
        if not visited[i]:
            temp = ""

            for ii in range(len(target)):
                if visited[ii] or i == ii:
                    temp += target[ii]

            if tmp > temp:
                tmp = temp
                tmp_idx = i

    visited[tmp_idx] = True
    print(tmp)
    recursion()


recursion()
