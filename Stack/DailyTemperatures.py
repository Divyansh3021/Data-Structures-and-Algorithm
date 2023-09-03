temperatures = [73,74,75,71,69,72,76,73]

stack = []
answers = []
days = 0

for i in range(len(temperatures)):
    if stack and temperatures[i] > stack[-1]:
        stack.append(temperatures[i])
        days += 1
        answers.append(days)

    elif stack and temperatures[i] < stack[-1]:
        n = 0
        while n < (len(temperatures)-i+1) and temperatures[i] < stack[-1]:
            days+=1
    