class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def setIsValid(hasdfh: List[str]) -> bool:
            row = [x for x in hasdfh if x != "."]
            for i in range (1,10):
                if (str(i) in row):
                    row.remove(str(i))
                
            if (row != []):
                return False
            return True
        
        for i in range(0,9):
            if(not setIsValid(board[i])):
                return False
            temp = [board[j][i] for j in range(0,9)]
            if(not setIsValid(temp)):
                return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                temp = []
                for i in range(box_row,box_row+3):
                    for j in range(box_col,box_col+3):
                        temp.append(board[i][j])
                if (not setIsValid(temp)):
                    return False
            
        return True
        


        
        