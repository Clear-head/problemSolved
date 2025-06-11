import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

if n == 2:
    print(1)
    sys.exit()
elif n == 1:
    print(0)
    sys.exit()

num = deque()
num.append(int(sys.stdin.readline().rstrip()))


ans = 0
for i in range(n - 1):

    next_person = int(sys.stdin.readline().rstrip())

    if next_person > num[-1]:
        cnt = 1

        while len(num) > 1:
            top = num.pop()

            if num[-1] > top:
                ans += sum([j for j in range(2, cnt + 2)])
                cnt = 1
            
            else:
                cnt += 1

        if num[0] < next_person:
            if cnt == 1:
                ans += 1
                
            else:
                cnt += 1
                ans += sum([j for j in range(2, cnt + 2)])
            
            num.pop()

        elif num[0] > next_person:
            if cnt != 1:
                for _ in range(cnt-1):
                    num.append(num[0])

    num.append(next_person)
    
if len(num) == 2:
    ans += 1
else:
    cnt = 1
    tmp = num.pop()
    while num:
        if num[-1] > tmp:
            ans += 1
            tmp = num.pop()
            continue

        num.pop()
        cnt += 1
    ans += sum([i for i in range(1, cnt)])
    



print(f"num: {num}")
print(ans)
