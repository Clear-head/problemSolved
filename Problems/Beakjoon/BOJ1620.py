from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

pocketMon = {}

for i in range(1, n+1):
    name = stdin.readline().strip()
    pocketMon[str(i)] = name
    pocketMon[name] = str(i)

output = []

for _ in range(m):
    stdout.write(pocketMon[stdin.readline().strip()] + '\n')
