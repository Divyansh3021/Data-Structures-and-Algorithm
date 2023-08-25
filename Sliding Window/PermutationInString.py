s1 = "adc"
s2 = "dcdafsa"

# window = ""
# num = 0
# first_element = s2[num]

# for i in range(len(s2)):
#     if len(window) > len(s1):
#         window = window.replace(first_element, "")
#         num += 1
#         first_element = s2[num]

#     print("Current element: ",s2[i])
#     print("first element: ",first_element)
#     print("Sorted S1: ",sorted(s1))
#     print("Sorted window: ",sorted(window),"\n\n")
#     if sorted(s1) == sorted(window):
#         print(True)
    
#     window += s2[i]

# else:
#     print(False)
    

s1count, s2count = [0]*26, [0]*26

for i in range(len(s1)):
    s1count[ord(s1[i]) - ord("a")] += 1
    s2count[ord(s2[i]) - ord("a")] += 1

matches = 0

for j in range(26):
    if s1count[j] == s2count[j]:
        matches+=1

print("s1count: ",s1count)
print("s2count: ",s2count)
print("Initial matches are: ",matches)

for k in range(len(s2)-len(s1)):
    print("Current element: ",s2[len(s1)+k])
    if matches== 26 :
        print(True)
    first_element = s2[k]
    print("First element: ",first_element,"\n\n\n")
    s2count[ord(first_element)-ord("a")] -= 1
    if first_element in s1:
        print("match decreased\n")
        matches-=1
    last_element = s2[len(s1)+k]
    s2count[ord(last_element)-ord("a")] += 1
    if last_element in s1:
        print("match increased\n")
        matches+=1

else:
    print(False)