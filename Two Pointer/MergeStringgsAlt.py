word1 = "abcdef"
word2 = "pqrs"
res_word = ""

for i in range(len(word1)):
    res_word += word1[i]
    
    while i < len(word2):
        # print(i)
        res_word += word2[i]
        break

if len(word2) > len(word1):
    for i in range(len(word2)-len(word1)):
        res_word += word2[len(word1)+i]

print(res_word)