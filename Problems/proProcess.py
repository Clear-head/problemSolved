
"""

    프로그래머스 lv2 프로세스

"""

from collections import deque


def solution(priorities, location):
    A = 97
    cnt = 0
    max_list = sorted(priorities, reverse=True)
    max_value = max(priorities)
    max_idx = 0
    answer = []
    target = 0

    for i in range(len(priorities)):
        answer.append([chr(A + i), priorities[i]])
        if i == location:
            target = answer[i][0]

    answer = deque(answer)
    while True:
        if answer[0][1] == max_value:
            tmp = answer.popleft()

            if tmp[0] == target:
                return cnt + 1
            else:
                max_idx += 1
                max_value = max_list[max_idx]
            cnt += 1
        elif answer[0][1] < max_value:
            answer.append(answer.popleft())
