from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        finalWord = defaultdict(list)
        currentRow = 1
        movement = "up"
        lenght = len(s)
        for x in range (lenght):
            print(currentRow)
            print(movement)
            finalWord[currentRow].append(s[x]) 
            if movement == "up":
                if currentRow == numRows:
                    
                    movement = "down"
                    currentRow -= 1
                    continue
                currentRow += 1
            else:
                
                if currentRow == 1:
                    
                    movement = "up"
                    currentRow += 1
                    continue
                currentRow -= 1
            
        strFinal = ""
        for x in finalWord.values():
            temp = ""
            for s in x:
                temp += s               
            strFinal = strFinal + temp
        print(strFinal)
        return strFinal



obj = Solution()
 
obj.convert("PAYPALISHIRING",3)