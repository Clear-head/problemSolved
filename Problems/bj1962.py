import unicodedata
import sys
import charset_normalizer
from charset_normalizer import from_bytes


def normalize_string(s):
    if isinstance(s, bytes):
        s = str(from_bytes(s).best())
    return unicodedata.normalize('NFD', s)


for _ in range(int(sys.stdin.readline().rstrip())):

    cardinal_1 = {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    cardinal_2 = {10: '십', 100: '백', 1000: '천'}
    cardinal_3 = {
        10 ** 4: '만', 10 ** 5: '억', 10 ** 6: '조', 10 ** 7: '경'
        , 10 ** 8: '해', 10 ** 9: '자', 10 ** 10: '양', 10 ** 11: '구'
        , 10 ** 12: '간', 10 ** 13: '정', 10 ** 14: '재', 10 ** 15: '극'
    }

    n, m = map(int, sys.stdin.readline().rstrip().split())

    non_use = list(map(str, sys.stdin.readline().rstrip().split()))

    for a in [cardinal_1, cardinal_2, cardinal_3]:
        del_item = []
        for key, value in a.items():
            normalized_value = normalize_string(value)

            for char in normalized_value:
                for target in non_use:
                    normalized_target = normalize_string(target)
                    if char == normalized_target:
                        del_item.append(key)
        for i in del_item:
            a.pop(i, None)

    print(cardinal_1)
    print(cardinal_2)
    print(cardinal_3)

    if cardinal_1 == {}:
        print(-1)
        continue
    tmp = 0
    ans = 0
    flag = False

    while True:
        tmp += 1

        if tmp % 10 not in cardinal_1.keys():
            continue

        if n == tmp:
            print(tmp)
            break

    print('123')
