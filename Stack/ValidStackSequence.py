pushed = [1,0]
popped = [1,0]

from collections import deque

stack = deque()

push_index = 0
pop_index = 0

for i in pushed:
    stack.append(i)
    while (pop_index<len(popped)) and stack and (popped[pop_index] == stack[-1]) :
        stack.pop()
        pop_index += 1

print(not stack) 
# if len(stack) == 0:
#     print(True)
# else:
#     print(False)