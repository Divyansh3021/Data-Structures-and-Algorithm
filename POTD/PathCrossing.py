#------------------Problem: 1496--------------------

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = {(0,0)}
        x,y = 0,0

        for char in path:
            if char == "N":
                y += 1
            elif char == "E":
                x += 1
            elif char == "W":
                x -= 1
            else:
                y -= 1
            
            if (x,y) in visit:
                return True
            visit.add((x,y))
        return False