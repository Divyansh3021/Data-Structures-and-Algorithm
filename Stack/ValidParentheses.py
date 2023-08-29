s = "()"

from collections import deque

stack = deque()

for i in range(len(s)):
    if (s[i] == "(") or (s[i]=="[") or (s[i] == "{"):
        stack.append(s[i])

    elif len(stack) > 0 and stack[-1] == "(" and s[i] == ")":
        stack.pop()
        
    elif len(stack) > 0 and stack[-1] == "[" and s[i] == "]":
        stack.pop()

    elif len(stack) > 0 and stack[-1] == "{" and s[i] == "}":
        stack.pop()
    
    else:
        stack.append(s[i])

if len(stack) == 0:
    print(True)

else:
    print(False)