# https://leetcode.com/problems/sort-array-by-parity-ii/


class Solution:
    def sortArrayByParityII(self, A):
        mid = len(A)//2
        for i in range(1,len(A),2):
            A.insert(i, A.pop())
        return A
        #
        # mid = len(A)//2
        # odd = A[:mid]
        # even = A[mid:]
        # for i in range(1, len(A), 2):
        #     odd.insert(i, even.pop(0))
        # return odd


s = Solution()
print(s.sortArrayByParityII([2,4,6,8,10,1,3,5,7,9]))