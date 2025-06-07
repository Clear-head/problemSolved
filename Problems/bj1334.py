
"""

    완성

"""

import sys

num = list(map(int, sys.stdin.readline().rstrip()))


def all_nine(num_list):
    if set(num_list) == {9}:
        # num_list = [0] * (len(num_list) + 1)
        # num_list[0] = 1
        # num_list[-1] = 1
        print(''.join(map(str, num_list)))
        return sys.exit()


def round_up(num_list, index):
    while True:
        for i in range(index, -1, -1):
            if num_list[i] != 9:
                num_list[i] = num_list[i] + 1
                break
            else:
                if i == 0:
                    num_list.insert(0, 1)
                num_list[i] = 0
        all_nine(num_list)
        if num_list[len(num_list) - 1] != 0:
            break

    return num_list


def is_palindrome(num_list):
    left = 0
    right = len(num_list) - 1

    while left < right:

        if num_list[left] > num_list[right]:
            num_list[right] = num_list[left]
            left += 1
            right -= 1

        elif num_list[left] < num_list[right]:

            if num_list[right] == 9:
                num_list = round_up(num_list, right)
                left = 0
                right = len(num_list) - 1

            else:

                if num_list[right - 1] != 9 and right - left != 1:
                    num_list[right - 1] += 1
                    num_list[right] = num_list[left]
                    left += 1
                    right -= 1

                elif num_list[right - 1] != 9 and right - left == 1:
                    num_list[right - 1] += 1
                    num_list[right] = num_list[left]
                    left = 0
                    right = len(num_list) - 1

                else:
                    num_list = round_up(num_list, right)
                    left = 0
                    right = len(num_list) - 1
        else:
            left += 1
            right -= 1

    return num_list


if len(num) == 1 and num[0] != 9:
    num[0] += 1
else:
    if num[len(num) - 1] == 9:
        if len(set(num)) != 1:
            num = round_up(num, len(num) - 1)
        else:
            num = [0] * (len(num) + 1)
            num[0] = 1
    else:
        num[len(num) - 1] += 1
    all_nine(num)
    num = is_palindrome(num)

print(''.join(map(str, num)))
