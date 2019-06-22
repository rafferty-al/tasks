#keys and rooms
#https://leetcode.com/problems/keys-and-rooms/description/
import collections

rooms = [
    [1,2],
    [2],
    [3],
    []
]

#defdict = collections.defaultdict(int)

'''for i in range(len(rooms)):
    if len(rooms[i]) == 0:
        defdict[i] = 1001
    for j in range(len(rooms[i])):
        defdict[i] = rooms[i][j]'''
keys = rooms[0]
