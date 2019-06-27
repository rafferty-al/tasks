# https://leetcode.com/problems/search-insert-position/
# Runtime: 36 ms, faster than 79.84% of Python3 online submissions for Search Insert Position.

def searchInsert(nums, target):
    index = 0
    for num in range(len(nums)):
        if nums[num] == target:
            index = num
            break
        else:
            index = None
    if index is None:
        for num in range(len(nums)):
            if target == 0:
                index = 0
                break
            elif nums[num] >= target:
                index = num
                break
            else:
                index = len(nums)
    return index


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 2))