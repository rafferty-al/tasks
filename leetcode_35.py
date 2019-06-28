# https://leetcode.com/problems/search-insert-position/
# Runtime: 40 ms, faster than 31.78% of Python3 online submissions for Search Insert Position.

def searchInsert(nums, target):
    index = 0
    for num in range(len(nums)):
        if nums[num] == target:
            index = num
            break
        else:
            if nums[num] <= target:
                index = num + 1
    return index


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 0))