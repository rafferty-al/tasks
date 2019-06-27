# https://leetcode.com/problems/merge-two-sorted-lists/
# Runtime: 40 ms, faster than 88.82% of Python3 online submissions for Merge Two Sorted Lists.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    merge = node = ListNode(0)
    l,r = True, True
    while l or r:
        v1 = getattr(l1, 'val', 'end')
        v2 = getattr(l2, 'val', 'end')
        if v2 == 'end' and v1 != 'end':
            node.next = ListNode(v1)
            node = node.next
            l1 = getattr(l1, 'next', None)
        elif v1 == 'end' and v2 != 'end':
            node.next = ListNode(v2)
            node = node.next
            l2 = getattr(l2, 'next', None)
        elif v1 < v2:
            node.next = ListNode(v1)
            node = node.next
            l1 = getattr(l1, 'next', None)
        elif v2 < v1:
            node.next = ListNode(v2)
            node = node.next
            l2 = getattr(l2, 'next', None)
        elif v1 == v2 and 'end' not in (v1,v2):
            node.next = ListNode(v1)
            node = node.next
            node.next = ListNode(v1)
            node = node.next
            l1 = getattr(l1, 'next', None)
            l2 = getattr(l2, 'next', None)
        if v1 == v2 == 'end':
            l, r = False, False
    return merge.next

def stringToListNode(input):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(int(number))
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

if __name__ == '__main__':
    l1 = '9'
    l2 = '548'

    n = merge_two_lists(stringToListNode(l1),stringToListNode(l2))
    print(listNodeToString(n))
