from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
tmp = sorted(list(set(stdin.readline() for _ in range(n)) & set(stdin.readline() for _ in range(n))))
stdout.write(str(len(tmp)) + '\n')
for i in tmp:
    stdout.write(i)
