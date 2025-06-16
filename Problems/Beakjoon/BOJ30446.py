
"""

    해야함
    시간초과 해결요망

"""

from collections import deque
import sys


# def solution1():
#     def is_palindrome(num):
#         string = deque(str(num))

#         while len(string) > 1:
#             print(string)
#             if string.pop() != string.popleft():
#                 return 0
            
#         return 1

#     n = int(sys.stdin.readline().rstrip())

#     cnt = 0
#     for i in range(1, n+1):
#         cnt += is_palindrome(i)

#     print(cnt)
sys.set_int_max_str_digits(1000000000)
n = int(sys.stdin.readline().rstrip())
if n < 10:
    print(n)
    sys.exit()

cnt = 9

def even_palindrome(q):
    global cnt

    if not q:
        for i in range(10):
            if int(str(i) + str(i)) <= n:
                q.append(str(i))
                cnt += 1

    tmp = deque()
    while q:
        num = q.popleft()
        for i in range(10):
            chk = num+str(i)

            if int(chk + chk[::-1]) <= n:
                tmp.append(chk)
                cnt += 1
            else:
                break
    return tmp


def odd_palindrome(q):
    tmp = deque()
    

# odd_palindrome(deque([str(i) for i in range(10)]))
even = even_palindrome(deque())
while even:
    even = even_palindrome(even)


print(cnt)

