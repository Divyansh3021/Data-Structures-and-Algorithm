s = "leet**cod*e"

from collections import deque

stack = deque()

for i in s:
    stack.append(i)

for i in stack:
    if i == "*":
        stack.pop()
        stack.pop()

print(stack)