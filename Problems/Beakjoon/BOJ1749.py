from sys import stdin

n, m = map(int, stdin.readline().split())
nums = [list(map(int, stdin.readline().split())) for _ in range(n)]

ans = -10001

for i in range(n):
    for ii in range(m):
        ans = max(ans, nums[i][ii])
        if i > 0 and ii > 0:
            nums[i][ii] += (nums[i-1][ii] + nums[i][ii-1] - nums[i-1][ii-1])
        elif i > 0 and ii == 0:
            nums[i][ii] += nums[i-1][ii]
        elif i == 0 and ii > 0:
            nums[i][ii] += nums[i][ii - 1]

for i in range(n-1, 0, -1):
    for ii in range(m-1, 0, -1):
        for j in range(i-1, 0, -1):
            for jj in range(ii-1, 0, -1):
                ans = max(ans, nums[i][ii] - nums[j][ii] - nums[i][jj] + nums[j][jj])
print(ans)
#
# from sys import stdin
#
# n, m = map(int, stdin.readline().split())
# nums = [list(map(int, stdin.readline().split())) for _ in range(n)]
#
#
# def kadane_1d(arr):
#     """
#     1차원 카데인 알고리즘: 주어진 1차원 배열에서 최대 부분 배열 합을 찾습니다.
#     """
#     max_so_far = float('-inf')
#     current_max = 0
#
#     for x in arr:
#         current_max += x
#         if current_max > max_so_far:
#             max_so_far = current_max
#         if current_max < 0:
#             current_max = 0  # 음수가 되면 초기화 (더하는 의미가 없으므로)
#     return max_so_far
#
#
# def kadane_2d(matrix):
#
#     ans = float('-inf')  # 전체 최대 합을 저장
#
#     # 1. 각 열 쌍 (left_col, right_col)을 선택
#     for left_col in range(m):
#         # current_row_sum: 각 행에 대한, left_col부터 right_col까지의 부분 합을 저장하는 임시 1차원 배열
#         temp_row_sums = [0] * n
#
#         for right_col in range(left_col, m):
#             # 2. 행 압축: left_col부터 right_col까지의 합을 각 행에 대해 계산하여 temp_row_sums 갱신
#             for row in range(n):
#                 temp_row_sums[row] += matrix[row][right_col]
#
#             # 3. 1차원 카데인 알고리즘 적용: temp_row_sums 배열에서 최대 부분 배열 합을 찾음
#             current_max_for_cols = kadane_1d(temp_row_sums)
#
#             # 4. 전체 최댓값 갱신
#             if current_max_for_cols > ans:
#                 ans = current_max_for_cols
#
#     return ans
#
#
# result = kadane_2d(nums)
# print(result)

from sys import stdin

n, m = map(int, stdin.readline().split())
nums = [list(map(int, stdin.readline().split())) for _ in range(n)]

result = -float('inf')

prefixSum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + nums[i - 1][j - 1]

for y1 in range(1, n + 1):
    for y2 in range(y1, n + 1):
        current_sum = 0

        for x in range(1, m + 1):
            col_sum = prefixSum[y2][x] - prefixSum[y1 - 1][x] - prefixSum[y2][x - 1] + prefixSum[y1 - 1][x - 1]
            current_sum += col_sum

            if current_sum > result:
                result = current_sum

            if current_sum < 0:
                current_sum = 0

print(result)
