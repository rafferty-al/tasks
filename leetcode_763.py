# https://leetcode.com/problems/partition-labels/
from string import ascii_lowercase
from random import choice


class Solution:
    def partitionLabels(self, S):
        groups = []
        group = False
        d = {}
        last_max_pos = 0
        for i in range(len(S)):
            if S.count(S[i]) == 1:
                if not group:
                    groups.append(S[last_max_pos:i + 1])
                    last_max_pos = i + 1
            else:
                group = True
                if S[i] not in d.keys():
                    d[S[i]] = S.rfind(S[i])
                    max_position = max(d.values())
                else:
                    if i == max_position:
                        groups.append(S[last_max_pos:i+1])
                        last_max_pos = max_position + 1
                        max_position = 0
                        d = {}
                        group = False
                    else:
                        continue
        return [len(s) for s in groups]


if __name__ == '__main__':
    # randstr = ''.join([choice(ascii_lowercase) for i in range(25)])
    randstr = 'ababcbacadefegdehijhklij'
    # randstr = "caedbdedda"
    s = Solution()
    print(s.partitionLabels(randstr))
    # print(s.get_max_pos('abcdef','a',0))