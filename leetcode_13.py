# https://leetcode.com/problems/roman-to-integer/
# я твой рот ебал

def romanToInt(s):
    numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    count, i = 0, 0
    if len(s) > 1:
        count = 'sasat'
    else:
        count = numbers[s[0]]
    return count

if __name__ == '__main__':
    letters = ['MCMXCIV', 'III', 'IV', 'IX', 'LVIII', 'MDCXCV','D']
    same_lett = ['I', 'II', 'III', 'V', 'VV', 'VVV', 'XXXXX']
    for i in same_lett:
        print(romanToInt(i))

