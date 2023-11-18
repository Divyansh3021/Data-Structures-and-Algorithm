#-------Problem: 473-------
#T.C. = O(4^n)

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4

        if sum(matchsticks) % 4 != 0:
            return False
        matchsticks.sort(reverse = True)

        def backtrack(index):
            if index == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[index] <= length:
                    sides[j] += matchsticks[index] 

                    if backtrack(index + 1):
                        return True
                    
                    sides[j] -= matchsticks[index]
            return False

        return backtrack(0)