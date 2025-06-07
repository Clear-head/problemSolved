"""

    미완성 글램팬

"""

import sys

text = list(map(str, sys.stdin.readline().rstrip()))

#   만약 알파벳 최소 수 못 맞추면 0 프린트 후 종료
if len(set(text)) < 26:
    print(0)
    sys.exit()


# 해시에 넣어서 빠진 알파벳 있으면 하단의 abc_dic.values() 로 찾아서 0 프린트 후 종료
abc_dic = {
    "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
    "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
    "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0
}

for i in text:
    abc_dic[i] += 1

if 0 in abc_dic.values():
    print(0)
    sys.exit()


"""

    여기부터 최소 조건 맞춘 후 작동하는 본문
    
"""

a_tmp = 0   # 맨 앞 A 갯수 체크
cnt = 0     # 글램팬 갯수 저장
index = 0   # 아스키 코드를 통해 65(A) 부터 1씩 더해 90(Z) 까지 가기 위한 변수

for i in range(len(text)):

    if text[i] == "A" and index != 90:  # A 찾으면 시작
        index = 65

    # index 90 까지 왔는데 Z 또 있을 떄 A 갯수 * Z 갯수 안하고 A 갯수 만큼 Z 나올때 마다 체크
    elif index == 90 and text[i] == "Z":
        cnt += a_tmp
        continue

    # 이전에 Z 까지 갔을 때 A 갯수 저장 해둔 변수까지 초기화
    elif text[i] == "A" and index == 90:
        index = 65
        a_tmp = 0

    # 아스키 코드상으로 ABC 나 ABBC 는 가능하지만 ABD 나 ABCDEB 일 경우 다시 세는 필터
    if ord(text[i]) - index > 1 or ord(text[i]) < index:
        index = 0
        a_tmp = 0

        # 근데 A 부터 세도 Z 까지 못가는 경우 끝
        if len(text) - i < 26:
            break

    # 맨 앞 A가 여러번 인 경우 체크
    elif index == ord(text[i]) == 65:
        a_tmp += 1

    # ABCD 처럼 순서대로 일 경우 아스키코드 + 1
    elif ord(text[i]) - index == 1:
        index += 1

    # A 부터 Z 까지 갔을 때 글램팬이므로 맨앞 A 갯수 만큼 체크
    if index == 90:
        cnt += a_tmp

print(cnt)
