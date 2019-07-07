# https://leetcode.com/problems/string-to-integer-atoi/
# пошло ты нахуй, ебаное задание

import re
import string


def myAtoi(str):
    num = 0
    key = {
        1: 1,
        2: 10,
        3: 100,
        4: 1000,
        5: 10000,
        6: 100000,
        7: 1000000,
        8: 10000000,
        9: 100000000,
        10: 1000000000
    }
    a = re.search('([+-][+-])+', str)
    b = re.search('(\s*[A-Za-z]+\s*)+\d', str)
    c = re.search('(^[.]\d)', str)
    if str == '' or a or b or c:
        return 0
    negative = True if re.search('-', str) else False
    match = re.search('[1-9]\d*', str)
    if match is None:
        return 0
    else:
        match = match.group()
    if int(match) < 2147483648:
        size = len(match)
        for i in match:
            num += int(i) * key[size]
            size -= 1
    else:
        num = 2147483648
    return num if not negative else num * -1


if __name__ == '__main__':
    print(myAtoi(" -0012a42"))

sas = "    +0a32"
