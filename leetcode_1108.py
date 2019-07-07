# https://leetcode.com/problems/defanging-an-ip-address/
# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Defanging an IP Address.


def defangIPaddr(address):
    return '[.]'.join(address.split('.'))