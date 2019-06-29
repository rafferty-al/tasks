# https://leetcode.com/problems/squares-of-a-sorted-array/
# Runtime: 152 ms, faster than 97.93% of Python3 online submissions for Squares of a Sorted Array.


def sortedSquares(A):
    for i in range(len(A)):
        A[i] = A[i] * A[i]
    return sorted(A)