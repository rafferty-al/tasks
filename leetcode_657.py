# https://leetcode.com/problems/robot-return-to-origin

def judgeCircle(moves):
    x, y = 0, 0
    for i in moves:
        if i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        elif i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
    return x == 0 and y == 0
    # return (moves.count("U") == moves.count("D")) and (moves.count("L") == moves.count("R"))