# https://leetcode.com/problems/remove-outermost-parentheses/


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def lastElem(self):
        return self.items[-1]

    def printS(self):
        print(self.items)


def remove(str):
    stack = Stack()
    for i in str:
        stack.push(i)

if __name__ == '__main__':
    s = '(()())(())'
    print(remove(s))
