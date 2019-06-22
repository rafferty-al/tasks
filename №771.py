#Jewels and stones
#https://leetcode.com/problems/jewels-and-stones/description/
J, S = list(input().split())
cnt = 0
for i in S:
    if i in J:
        cnt += 1
print(cnt)