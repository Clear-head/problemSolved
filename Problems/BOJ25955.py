
"""

    완성

"""

import sys

n = int(sys.stdin.readline().rstrip())
lv = list(map(str, sys.stdin.readline().rstrip().split(" ")))


def return_tier(text):
    tier = ["B", "S", "G", "P", "D"]
    return tier.index(text)


def sort_list(li):
    return sorted(li, key=lambda x: (return_tier(x[0]), -int(x[1:])))


ans_list = sort_list(lv)

if lv == ans_list:
    print("OK")
else:

    ans = []
    print("KO")
    for i in range(n):
        if lv[i] != ans_list[i]:
            ans.append(lv[i])
    ans = sort_list(ans)
    print(ans[0], ans[1])



