# В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа, которым они соответствуют в десятичной системе счисления):
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
# Формат ввода:
# Строка, содержащая натуральное число nn, 0 < n < 40000<n<4000.
# Формат вывода:
# Строка, содержащая число, закодированное в римской системе счисления.

number = int(input())
cp = number
discharge, nums, result = 1, set(), set()
roman_nums = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
}
while cp > 0:
    curr = cp % 10
    cp = cp // 10
    nums.add(curr * discharge)
    discharge = discharge * 10

for i in sorted(nums, reverse=True):
    if roman_nums.get(i, None):
        result.add(roman_nums[i])
    else:
        continue


