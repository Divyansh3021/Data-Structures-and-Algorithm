s = "ebcbbececabbacecbbcbe"
new_s = ""
for char in s:
    if char.isalnum():
        new_s+=char.lower()

i = 0
j = len(new_s) - 1
count = 0
print(new_s)
while i <= j:
    # print("new_s[i]: ",new_s[i]," new_s[j]: ",new_s[j])
    if new_s[i] == new_s[j]:
        i+=1
        j-=1
    elif (new_s[i] != new_s[j]) and (count==0):
        if (new_s[i+1] == new_s[j]):
            new_s.replace(new_s[i], "")
            i+=1
        elif (new_s[i] == new_s[j-1]):
            new_s.replace(new_s[j], "")
            j-=1
        else:
            print(False)
        count+=1
    else:
        print(False)
        break

print(True)