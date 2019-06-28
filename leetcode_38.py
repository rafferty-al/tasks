# https://leetcode.com/problems/count-and-say/

def countAndSay(n):
    init = '1'
    for i in range(n):
        c = 0
        char = init[0]
        line = ''
        for i in range(len(init)):
            if init[i] != char:
                line += c + char
                init = init[c:]
            c += 1
        init = line
    return init


if __name__ == '__main__':
    print(countAndSay(2))