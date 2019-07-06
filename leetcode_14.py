# https://leetcode.com/problems/longest-common-prefix/
# Runtime: 32 ms, faster than 95.41% of Python3 online submissions for Longest Common Prefix.

def find(strs):
    res = ''
    if strs.__len__() == 0:
        return res
    for chars in zip(*strs):
        if chars.count(chars[0]) != len(chars):
            break
        res += chars[0]
    return res

# def find(strs):
#     if strs.__len__() == 0:
#         return ''
#     pref = strs[0]
#     for i in strs:
#         while i.find(pref) != 0:
#             pref = pref[:-1]
#             if pref == '':
#                 return pref
#     return pref


wrong = ['dog', 'racecar', 'car']  # ''
wrong2 = ["c","acc","ccc"]
well = ['flower', 'flow', 'flight']  # 'fl'

print(find(wrong2))