#Island Perimeter
#https://leetcode.com/problems/island-perimeter/description/
import sys
map = [list(map(int, i) for i in sys.stdin)]
dict= {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
sm = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            continue
        else:
            cnt=0
            for a in (-1,1):
                ai = i + a
                if 0 <= ai < len(map)and map[ai][j] == 1:
                    cnt+=1
            for b in (-1,1):
                aj = j + b
                if 0 <= aj < len(map[0]) and map[i][aj] == 1:
                    cnt += 1
            sm += dict[cnt]
print(sm)