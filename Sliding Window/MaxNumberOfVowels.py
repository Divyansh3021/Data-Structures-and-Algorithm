s = "leetcode"
k = 3

vowels = ['a','e','i','o','u']
l = 0
count = 0
max_count = 0

for r in range(len(s)):
    if (r-l+1) > k:
        if s[l] in vowels:
            count -= 1
        l += 1
    if s[r] in vowels:
        count+=1
    max_count = max(count, max_count)
    

print(max_count)