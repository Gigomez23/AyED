from stack import Stack

def is_balanced(expression):
    stack = Stack()
    opening = '({['
    closing = ')}]'
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False
    return stack.is_empty()