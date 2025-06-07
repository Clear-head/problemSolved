"""

    프로그래머스 "전력망을 둘로 나누기" 완성

"""

import sys
from collections import deque

INF = sys.maxsize


def bfs(start, graph):
    visited = set()
    q = deque([start])
    connect_node = []

    while q:
        base_node = q.popleft()

        if base_node not in visited:
            tmp = []
            visited.add(base_node)
            q.append(base_node)

            while q:
                tmp_node = q.popleft()
                tmp.append(tmp_node)

                for next_node in graph[tmp_node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        q.append(next_node)

            connect_node.append(tmp)

    return connect_node


def solution(n, wires):
    min_cnt = INF
    for i in range(n-1):
        g = [[] for _ in range(n + 1)]
        for ii in range(len(wires)):
            if ii != i:
                g[wires[ii][0]].append(wires[ii][1])
                g[wires[ii][1]].append(wires[ii][0])

        print(g)

        left = bfs(wires[i][0], g)
        right = bfs(wires[i][1], g)

        # print(left, right)
        # print(len(left[0]), len(right[0]))

        min_cnt = min(min_cnt, abs(len(left[0]) - len(right[0])))

    return min_cnt


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
