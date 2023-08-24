s1 = "adc"
s2 = "dcdafsa"

window = ""
num = 0
first_element = s2[num]

for i in range(len(s2)):
    if len(window) > len(s1):
        window = window.replace(first_element, "")
        num += 1
        first_element = s2[num]

    print("Current element: ",s2[i])
    print("first element: ",first_element)
    print("Sorted S1: ",sorted(s1))
    print("Sorted window: ",sorted(window),"\n\n")
    if sorted(s1) == sorted(window):
        print(True)
    
    window += s2[i]

else:
    print(False)
    