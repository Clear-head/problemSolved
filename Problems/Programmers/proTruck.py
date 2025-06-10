
"""

    다리를 지나는 트럭: 완료

"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    seq = 0
    time = 0
    dq = deque([])

    truck_cnt = len(truck_weights)

    already = 0

    while True:

        summ = 0
        time += 1

        if len(dq) > 0:
            for i in dq:
                i[1] += 1
                summ += i[0]

        if len(dq) > 0 and dq[0][1] >= bridge_length:

            dq.popleft()
            already += 1

        if summ + truck_weights[seq] <= weight and bridge_length > len(dq):
            dq.append([truck_weights[seq], 1])
            if seq + 1 < truck_cnt:
                seq += 1

        if already == truck_cnt:
            break

    return time + 1


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
