# https://leetcode.com/problems/search-insert-position/
# Runtime: 40 ms, faster than 31.78% of Python3 online submissions for Search Insert Position.

def searchInsert(nums, target):
    index = 0
    for num in range(len(nums)):
        if nums[num] == target:
            index = num
            break
        elif nums[num] <= target:
            index = num + 1
    return index


def binary_search(nums, target):
    begin = 0
    end = len(nums) - 1
    while (len(nums) > begin) and (end != 0) and (begin != end):
        mid = (begin + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            begin += 1
        else:
            end -= 1
    return begin


target = 555
nums = [1,3,5]


def binary_rec(begin,end):
    mid = (begin + end) // 2
    if len(nums) == begin or end == 0 or begin == end:
        index = begin
    elif nums[mid] == target:
        index = mid
    elif nums[mid] < target:
        index = binary_rec(begin + 1,end)
    else:
        index = binary_rec(begin, end - 1)
    return index

if __name__ == '__main__':
    # print(binary_search([1,3,5,6], 520))
    print(binary_rec(0, len(nums)))