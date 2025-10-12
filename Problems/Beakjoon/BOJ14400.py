from sys import stdin

n = int(stdin.readline())
customer = []
for _ in range(n):
    customer.append(tuple(map(int, stdin.readline().split())))

customer_x = sorted(customer, key=lambda x: x[0])
customer_y = sorted(customer, key=lambda x: x[1])

ans = 0

for i in customer:
    ans += abs(customer_x[n//2][0] - i[0]) + abs(customer_y[n//2][1] - i[1])

print(ans)