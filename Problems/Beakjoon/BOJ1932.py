from sys import stdin

triangle = []
n = int(stdin.readline().rstrip())

for _ in range(n):
    triangle.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(n-2, -1, -1):
    triangle[i] = [max(triangle[i + 1][j] + triangle[i][j], triangle[i + 1][j + 1] + triangle[i][j]) for j in range(len(triangle[i]))]

print(triangle[0][0])

