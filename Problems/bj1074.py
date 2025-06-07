import sys

N, ans_c, ans_r = map(int, sys.stdin.readline().rstrip().split(" "))


def recursion(c, r, cnt, h, w):
    """
    @param c: 작은 사각형 좌우
    @param r: 작은 사각형 상하
    @param cnt: 몇번째?
    @param h: 큰 사각형 상하
    @param w: 큰 사각형 좌우
    @return: ans_c == h, ans_r == w
    """

    global N

    if h == ans_c and w == ans_r:
        print(cnt)
        return

    # 좌 상단
    if c == 0 and r == 0:
        recursion(c + 1, r, cnt + 1, h, w + 1)

    # 우 상단
    elif c == 1 and r == 0:
        recursion(c - 1, r + 1, cnt + 1, h + 1, w - 1)

    # 좌 하단
    elif c == 0 and r == 1:
        recursion(c + 1, r, cnt + 1, h, w + 1)

    # 우 하단 경우의 수

    elif c == 1 and r == 1:

        """
        
            1 사분면
        
        """

        # 1 사분면 내부
        if h <= 2 ** N // 2 - 1 and w < 2 ** N // 2 - 1:
            recursion(c - 1, r - 1, cnt + 1, h - 1, w + 1)

        # 1 사분면 오른쪽 끝에만 닿았을 때
        elif h < 2 ** N // 2 - 1 and w == 2 ** N // 2 - 1:
            recursion(0, 0, cnt + 1, h + 1, 0)

        # 1 사분면 오른쪽 끝, 아래쪽 끝에 닿았을 때
        elif h == 2 ** N // 2 - 1 and w == 2 ** N // 2 - 1:
            recursion(0, 0, cnt + 1, 0, w + 1)

        #
        # 2 사분면
        #

        # 2 사분면 내부
        elif h <= 2 ** N // 2 - 1 and w < 2 ** N - 1:
            recursion(c - 1, r - 1, cnt + 1, h - 1, w + 1)

        # 2 사분면 오른쪽 끝에만 닿았을 때
        elif h < 2 ** N // 2 - 1 and w == 2 ** N - 1:
            recursion(0, 0, cnt + 1, h + 1, 2 ** N // 2)

        # 2 사분면 오른쪽 끝, 아래쪽 끝에 닿았을 때
        elif h == 2 ** N // 2 - 1 and w == 2 ** N - 1:
            recursion(0, 0, cnt + 1, h + 1, 0)

        #
        # 3 사분면
        #

        # 3 사분면 내부
        elif h > 2 ** N // 2 - 1 > w:
            recursion(c - 1, r - 1, cnt + 1, h - 1, w + 1)

        # 3 사분면 오른쪽 끝에만 닿았을 때
        elif h > 2 ** N // 2 - 1 and w == 2 ** N // 2 - 1:
            recursion(0, 0, cnt + 1, h + 1, 0)

        # 3 사분면 오른쪽 끝, 아래쪽 끝에 닿았을 때
        elif h == 2 ** N - 1 and w == 2 ** N // 2 - 1:
            recursion(0, 0, cnt + 1, 2 ** N // 2, w + 1)

        #
        # 4 사분면
        #

        # 4 사분면 내부
        elif h > 2 ** N // 2 - 1 and 2 ** N // 2 - 1 < w:
            recursion(c - 1, r - 1, cnt + 1, h - 1, w + 1)

        # 4 사분면 오른쪽 끝에만 닿았을 때
        elif h > 2 ** N // 2 - 1 and w == 2 ** N - 1:
            recursion(0, 0, cnt + 1, h + 1, 2 ** N // 2)

        # 4 사분면 오른쪽 끝, 아래쪽 끝에 닿았을 때
        elif h == 2 ** N - 1 and w == 2 ** N - 1:
            print(cnt)


recursion(0, 0, 0, 0, 0)
