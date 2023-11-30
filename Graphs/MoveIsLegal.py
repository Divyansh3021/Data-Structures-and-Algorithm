#---------------Problem: 1958--------------

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ROWS, COLS = 8, 8
        directions = [[1,0], [-1,0],[0,1], [0,-1], [1,1],[1,-1],[-1, 1],[-1,-1]]
        board[rMove][cMove] = color

        def legal(row, col, color, direction):
            dr, dc = direction
            row, col = row + dr, col + dc
            length = 1

            while (0 <= row < ROWS) and (0 <= col < COLS):
                length += 1

                if board[row][col] == ".": return False
                if board[row][col] == color:
                    return length >= 3
                
                row, col = row + dr, col + dc
            return False
        
        for d in directions:
            if legal(rMove, cMove, color, d):
                return True
        
        return False
