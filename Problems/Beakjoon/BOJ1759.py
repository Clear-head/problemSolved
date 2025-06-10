"""

    미완성

"""

import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().rstrip().split())
word = list(map(str, sys.stdin.readline().rstrip().split()))
gather = []

if l == c:
    word = sorted(list(word))
    print(''.join(word))
    sys.exit()

for i in word:
    if i in 'aeiou':
        gather.append(i)

for i in gather:
    word.remove(i)

ans = set()

for k in range(1, l-1):
    gather_combi = combinations(gather, k)

    for i in list(gather_combi):
        word_combi = combinations(word, l - k)
        for ii in list(word_combi):
            string = ''.join(list(i))
            string += ''.join(list(ii))
            ans.add(''.join(sorted(list(string))))

ans = sorted(list(ans))
for i in ans:
    print(i)
    if i == 'abcdefghijklmou':
        print('asd')




