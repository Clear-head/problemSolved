
"""

    미완

"""

import sys
# from collections import

tc = str(sys.stdin.readline().rstrip().split(""))

st = []
left = 0
right = 0

answer = 0

for i in tc:
    if i == "(":
        print()

        if len(st) == 0 or st[-1] == "(":
            st.append(i)
        elif st[-1] == ")":
            left += len(st)
            st.clear()
            st.append(i)

    else:
        if len(st) == 0:
            pass
        elif i == "(":
            right += len(st) + 1
            st.clear()
            st.append("(")
        else:
            pass
