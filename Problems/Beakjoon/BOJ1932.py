from sys import stdin

triangle = []
n = int(stdin.readline().rstrip())

for _ in range(n):
    triangle.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])
