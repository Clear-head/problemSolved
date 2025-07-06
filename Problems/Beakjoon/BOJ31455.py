from sys import stdin

# def recursive(left, right, top, bot, length):
#     sum_cookies = []
#
#     for i in range(top, bot):
#         for ii in range(left, right):
#             sum_cookies.append(cookie[i][ii])
#
#     c = sum(sum_cookies)
#     if length == 1:
#         answer.append(c)
#         return
#
#     mid_x = (left + right) // 2
#     mid_y = (top + bot) // 2
#
#     if c % 4 == 0:
#         recursive(mid_x, right, top, mid_y, length // 2)  # 우상단
#         recursive(left, mid_x, mid_y, bot, length // 2)  # 좌하단
#         recursive(mid_x, right, mid_y, bot, length // 2)  # 우하단
#
#     elif c % 4 == 1:
#         recursive(left, mid_x, top, mid_y, length // 2)  # 좌상단
#         recursive(left, mid_x, mid_y, bot, length // 2)  # 좌하단
#         recursive(mid_x, right, mid_y, bot, length // 2)  # 우하단
#
#     elif c % 4 == 2:
#         recursive(left, mid_x, top, mid_y, length // 2)  # 좌상단
#         recursive(mid_x, right, top, mid_y, length // 2)  # 우상단
#         recursive(mid_x, right, mid_y, bot, length // 2)  # 우하단
#     else:
#         recursive(left, mid_x, top, mid_y, length // 2)  # 좌상단
#         recursive(mid_x, right, top, mid_y, length // 2)  # 우상단
#         recursive(left, mid_x, mid_y, bot, length // 2)  # 좌하단
#
#
# T = int(stdin.readline())
# for _ in range(T):
#     n = int(stdin.readline())
#     cookie = []
#
#     answer = []
#
#     for u in range(n):
#         cookie.append(list(map(int, stdin.readline().rstrip())))
#
#     recursive(0, n, 0, n, n)
#     print(sum(answer))


# def recursive(left, right, top, bot):
#     if right - left == 1:
#         return cookie[top][left]
#
#     c = prefix_sum[bot][right] - prefix_sum[top][right] - prefix_sum[bot][left] + prefix_sum[top][left]
#
#     mid_x = (left + right) // 2
#     mid_y = (top + bot) // 2
#
#     all_quadrants = [
#         (left, mid_x, top, mid_y),  # 0: 좌상단
#         (mid_x, right, top, mid_y),  # 1: 우상단
#         (left, mid_x, mid_y, bot),  # 2: 좌하단
#         (mid_x, right, mid_y, bot)  # 3: 우하단
#     ]
#
#     skipped_index = c % 4
#
#     return sum(recursive(*coords) for y, coords in enumerate(all_quadrants) if y != skipped_index)
#
#
# T = int(stdin.readline())
# for _ in range(T):
#     n = int(stdin.readline())
#     cookie = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
#
#     prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             prefix_sum[i][j] = (cookie[i - 1][j - 1] +
#                                 prefix_sum[i - 1][j] +
#                                 prefix_sum[i][j - 1] -
#                                 prefix_sum[i - 1][j - 1])
#
#     result = recursive(0, n, 0, n)
#     print(result)
import sys

input = sys.stdin.readline

t = int(input())

def split_cookie(cookie):
    global cnt
    p = len(cookie)
    if p == 1:
        cnt += cookie[0][0]
        return

    total = sum(sum(row) for row in cookie)
    check = total % 4
    x = p // 2

    piece = [
        [row[:x] for row in cookie[:x]],
        [row[x:] for row in cookie[:x]],
        [row[:x] for row in cookie[x:]],
        [row[x:] for row in cookie[x:]]
    ]
    for i in range(4):
        if i == check:
            continue
        else:
            split_cookie(piece[i])


for _ in range(t):
    cnt = 0
    n = int(input())
    cookie = [list(map(int, input().rstrip())) for i in range(n)]
    split_cookie(cookie)
    print(cnt)
