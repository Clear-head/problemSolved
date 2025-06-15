import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

color_list = [0, 0]


def recursive(left, right, top, bot):
    color = paper[top][left]

    for i in range(top, bot):
        for j in range(left, right):
            if paper[i][j] != color:
                mid_x = (left + right) // 2
                mid_y = (top + bot) // 2
                recursive(left, mid_x, top, mid_y)  # 좌상단
                recursive(left, mid_x, mid_y, bot)  # 좌하단
                recursive(mid_x, right, top, mid_y)  # 우상단
                recursive(mid_x, right, mid_y, bot)  # 우하단
                return

    color_list[color] += 1
    return


recursive(0, n, 0, n)
print(color_list[0])
print(color_list[1])