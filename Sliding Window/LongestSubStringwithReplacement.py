s = "AABABBA"
k = 1

result = 0
count = {}

left = 0

for right in range(len(s)):
    count[s[right]] = 1 + count.get(s[right], 0)

    if (right-left+1) - max(count.values()) > k:
        count[s[left]] -= 1
        left += 1
    
    result = max(right-left+1, result)

print(result)