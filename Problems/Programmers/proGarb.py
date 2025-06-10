"""

    의상 완성

"""
from collections import Counter as counter


def solution(clothes):
    grab = []
    for i in clothes:
        grab.append(i[1])

    ans = len(grab)
    grab = counter(grab)
    tmp = 1

    if len(grab) == 1:
        return ans
    else:
        for i in grab.values():
            tmp += i * tmp
    return tmp - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
