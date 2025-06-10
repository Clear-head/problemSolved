# import sys
#
#
# def lower_bound(target, area):
#     start = 0
#     end = len(area)
#
#     while start < end:
#         mid = (start + end) // 2
#
#         if area[mid] <= target:
#             start = mid + 1
#         else:
#             end = mid
#
#     return len(area) - end
#
#
# n, h = map(int, sys.stdin.readline().split())
#
# bot = []  # 석순
# top = []  # 종유석
#
# obstacle = [0] * h
#
# for i in range(n//2):
#     bot.append(int(sys.stdin.readline().rstrip()))
#     top.append(int(sys.stdin.readline().rstrip()))
#
# bot.sort()
# top.sort()
#
# ans = sys.maxsize
# interval = 0
#
# for i in range(1, h + 1):
#     cnt = lower_bound(i - 1, bot) + lower_bound(h - i, top)
#
#     if cnt < ans:
#         ans = cnt
#         interval = 1
#     elif cnt == ans:
#         interval += 1
#
# print(ans, interval)

import sys

n, h = map(int, sys.stdin.readline().split())
obstacle = [0] * (h+1)
for i in range(n//2):
    tmp1 = int(sys.stdin.readline().rstrip())
    tmp2 = int(sys.stdin.readline().rstrip())

    """
    
        이 밑에 부분 기억해.
        양 끝에 최댓값, 원하는 인덱스에 -해주기
    
    """

    obstacle[0] += 1
    obstacle[tmp1] -= 1

    obstacle[h-tmp2] += 1
    obstacle[h] -= 1


for i in range(1, h+1):
    obstacle[i] += obstacle[i-1]
obstacle.pop()

print(min(obstacle), obstacle.count(min(obstacle)))
