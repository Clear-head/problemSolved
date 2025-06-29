import sys

n = int(sys.stdin.readline())

if n >= 1023:
    print(-1)
    sys.exit()

ans = [i for i in range(10)]


def func(li):
    if ans[-1] >= 9876543210:
        return
    tmp = []
    for i in li:
        for ii in range(int(str(i)[-1])):
            tmp.append(int(str(i) + str(ii)))

    ans.extend(tmp)
    func(tmp)


func(ans)

ans = sorted(ans)

print(ans[n])
