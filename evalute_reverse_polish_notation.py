from typing import List
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for x in tokens:
            match x:
                case "+":
                    
                    top = stack[-1]
                    secondTop = stack[-2]
                    topInt = int(top)
                    secondTopInt = int(secondTop)
                    
                    stack.pop()
                    stack.pop()
                    
                    stack.append(secondTopInt + topInt)
                    continue
                case "-":

                    top = stack[-1]
                    secondTop = stack[-2]
                    topInt = int(top)
                    secondTopInt = int(secondTop)
                    
                    stack.pop()
                    stack.pop()
                    
                    stack.append(secondTopInt - topInt)

                    continue
                case "*":

                    top = stack[-1]
                    secondTop = stack[-2]
                    topInt = int(top)
                    secondTopInt = int(secondTop)
                    print(top,secondTop)
                    stack.pop()
                    stack.pop()
                    stack.append(secondTopInt*topInt)
                    continue
                case "/":

                    top = stack[-1]
                    secondTop = stack[-2]
                    topInt = int(top)
                    secondTopInt = int(secondTop)
                    # print(top,secondTop)
                    stack.pop()
                    stack.pop()
                    
                    stack.append(math.trunc(secondTopInt / topInt))

                    continue
            
            stack.append(x)

        
        # print("Stack: ", stack)

        return stack[0]


obj = Solution()

obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])