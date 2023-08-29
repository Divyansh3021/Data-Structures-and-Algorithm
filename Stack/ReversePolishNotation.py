tokens = ["10"]

from collections import deque

stack = deque()
res = 0
for i in tokens:
    if i not in ["+","-","*","/"]:
        stack.append(i)
    else:
        num1 = int(stack.pop())
        num2 = int(stack.pop())

        if i == "+":
            res = num1+num2
            stack.append(res)
        elif i == "-":
            res = num2-num1
            stack.append(res)
        elif i == "*":
            res = num2*num1
            stack.append(res)
        elif i == "/":
            res = num2/num1
            stack.append(res)
    print("Current stack is: ",stack)
print(stack.pop())