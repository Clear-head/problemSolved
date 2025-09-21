ans = 1
for i in range(2, int(input())+1):
    ans = (ans * i) % (10**9 + 7)

print(ans)
