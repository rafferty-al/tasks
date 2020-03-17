from random import randrange, choice


def get_val(i, j):
    val = 0
    for i_sh in (-1, 0, 1):
        id = i + i_sh
        for j_sh in (-1, 0, 1):
            jd = j + j_sh
            if 0 <= id < n and 0 <= jd < m and not j_sh == i_sh == 0:
                val += field[i + i_sh][j + j_sh] == '*'
    return str(val)


n = m = randrange(2,10,1)
field = [[choice('.*') for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if field[i][j] != '*':
            field[i][j] = get_val(i, j)


for i in range(n):
    print(''.join(field[i]))