from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        temp = []
        final = ""

        while True:
            
            for x in strs:
                try:
                    temp.append(x[count])
                except:
                    return final

            print(temp)
            element = temp[0]
            for item in temp:
                if element != item:
                    print("Final: ", final)
                    return final
                    

            final = final + element
            temp = []
            count += 1

            






obj = Solution()

obj.longestCommonPrefix(["flower","flow","flight"])