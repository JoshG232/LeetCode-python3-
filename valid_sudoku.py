from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numBoard: List[List[int]] = self.convertBoard(board)
        result1 = self.checkGrid(numBoard)
        result2 = self.rowCheck(numBoard)
        result3 = self.columnCheck(numBoard)
        if (result1 == False or result2 == False or result3 == False):
            print("False")
            return False
        print("True")
        return True

    def convertBoard(self, board: List[List[str]]):
        # print("Converting grid")
        result = []
        for row in board:
            new_row = [int(cell.replace(".", "0")) for cell in row]
            result.append(new_row)
        return result
            
            
    def checkGrid(self, board: List[List[str]]):
        # print("Checking grid")
        subgrids = []
        finalBoard = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [row[j:j+3] for row in board[i:i+3]]
                subgrids.append(subgrid)
        for x in subgrids:
            newRow = [num for row in x for num in row]
            finalBoard.append(newRow)
        for j in finalBoard:
            print(j)
        result = self.rowCheck(finalBoard)
        print(result)
        if(result == False):
            return False
        
        

    def columnCheck(self, board: List[List[str]]):
        # print("Checking column")
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []
        row7 = []
        row8 = []
        row9 = []

        for row in board:
            row1.append(row[0])
            row2.append(row[1])
            row3.append(row[2])
            row4.append(row[3])
            row5.append(row[4])
            row6.append(row[5])
            row7.append(row[6])
            row8.append(row[7])
            row9.append(row[8])

        columnBoard = [row1,row2,row3,row4,row5,row6,row7,row8,row9]
        
        result = self.rowCheck(columnBoard)

        if(result == False):
            return False

        

    def rowCheck(self, board: List[List[int]]):
        # print("Checking row")
        
        for row in board:
            
            for number in range(1,10):

                amount = row.count(number)
                
                if amount <= 2:
                    
                    return False
                

    
obj = Solution()

obj.isValidSudoku([
                    [".",".",".","1",".","8",".",".","."],
                    [".",".",".",".",".",".",".",".","."],
                    [".",".",".",".",".",".",".",".","."],
                    ["4",".",".",".",".","7",".",".","."],
                    [".",".",".","7",".",".","8","4","1"],
                    [".",".",".",".","7",".",".",".","."],
                    [".",".",".",".",".",".","6",".","."],
                    [".",".",".","6",".",".",".",".","."],
                    ["6",".",".",".",".",".",".",".","."]
                ])



