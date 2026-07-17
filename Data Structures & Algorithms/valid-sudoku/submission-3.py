class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for column in range(9):
                if board[row][column] != '.':
                    if board[row][column] in seen :
                        return False
                    else:
                        seen.add(board[row][column])
        
        for column in range(9):
            seen = set()
            for row in range(9):
                if board[row][column] != '.':
                    if board[row][column] in seen :
                        return False
                    else:
                        seen.add(board[row][column])
        
        for row in range(0, 9, 3):
            #thats just 0, 3, 6
            for column in range(0, 9, 3):
                #same here
                seen = set()
                for boxrow in range(row, row+3, 1):
                    for boxcol in range(column, column+3, 1):
                        x = board[boxrow][boxcol]
                        if x != '.':
                            if x in seen :
                                return False
                            else:
                                seen.add(x)

        return True

                    
