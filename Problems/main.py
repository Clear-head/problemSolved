# import sys
#
# ans = 0  # 최대 타일 값
#
# import bj1334 as bj
#
# def main(n):
#     if n == n[::-1]:
#         print(n)
#     else:
#         while True:
#             if n == n[::-1]:
#                 # print(n)
#                 break
#             n = str(int(n) + 1)
#     return n
#
#
# if __name__ == "__main__":
#     n = str(sys.stdin.readline().rstrip())
#
#     while True:
#
#         if main(str(int(n)+1)) == bj.test(list(map(int, n))):
#             print("False")
#             print("main: " + main(str(int(n) + 1)))
#             print("bj: " + bj.test(list(map(int, n))))
#
#         n = str(int(n)+1)
#
#         if int(n)>999999:
#             break
