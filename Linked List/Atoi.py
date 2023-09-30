class Solution:
    def myAtoi(self, s: str) -> int:
        string = s.replace(" ","")
        result = 0
        flag = False
        for char in s:
            if char in ["1","2","3","4","5","6","7","8","9","0"]:
                result = result*10 + int(char)
            elif char in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"\n","."]:
                break
            elif char == "-" and result == 0:
                flag = True
            elif char == "-":
                result *= -1
                break
        if flag == True:
            result *= -1

        if result > 2**32 - 1:
            result = 2**32 - 1
        elif result < -2**31:
            result = -2**31
        return result