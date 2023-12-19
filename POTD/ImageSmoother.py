#-----------------------Problem: 661-----------------------------

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])  #ggetting the dimensions of array
        result = [[0] * cols for _ in range(rows)] #starting with an zero result array

        for i in range(rows): 
            for j in range(cols):
                total_sum = 0
                count = 0

                for x in range(max(0, i-1), min(rows, i+2)): #Iterating the available rows
                    for y in range(max(0, j-1), min(cols, j+2)):  #Iterating the available cols
                        total_sum += img[x][y]
                        count += 1

                result[i][j] = total_sum // count #counting the average

        return result