import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
nums = [sys.stdin.readline().strip() for _ in range(n)]

visited = [False] * n
ans = set()


def backtrack(depth, current_num_str):
    if depth == k:
        ans.add(current_num_str)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtrack(depth + 1, current_num_str + nums[i])
            visited[i] = False


backtrack(0, "")

print(len(ans))
