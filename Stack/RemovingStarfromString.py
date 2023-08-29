s = "leet**cod*e"

from collections import deque

stack = deque()

for i in s:
    if i == "*":
        stack.pop()
    else:
        stack.append(i)

string = ""
for i in stack:
    string += i

print(string)