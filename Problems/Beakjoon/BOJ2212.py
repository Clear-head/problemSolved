from sys import stdin


n = int(stdin.readline().rstrip())
k = int(stdin.readline().rstrip())
sensor = sorted(list(set(map(int, stdin.readline().rstrip().split()))))

if n <= k:
    print(0)
    exit()

road = max(sensor) - min(sensor)

cal = []
for i in range(len(sensor)-1):
    cal.append(sensor[i+1] - sensor[i])

cal = sorted(cal)

for i in range(k - 1):
    road -= cal.pop()

print(road)