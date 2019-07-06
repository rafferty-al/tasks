# https://leetcode.com/problems/to-lower-case/
# Runtime: 36 ms, faster than 69.68% of Python3 online submissions for To Lower Case.

def toLowerCase(str):
    res = ''
    for i in str:
        if 65 <= ord(i) <= 90:
            res += chr(ord(i) + 32)
        else:
            res += i
    return res

