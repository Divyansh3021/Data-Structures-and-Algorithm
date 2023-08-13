s = "A man, a plan, a canal: Panama"
new_s = ""
for char in s:
    if char.isalnum():
        new_s+=char.lower()

i = 0
j = len(new_s) - 1

print(new_s)
while i < j:
    if new_s[i] == new_s[j]:
        i+=1
        j-=1
    else:
        print(False)
        break

print(True)