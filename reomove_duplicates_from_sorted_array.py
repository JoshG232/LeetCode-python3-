from typing import List

class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        finalNums = []

        for x in nums: 
            if x not in finalNums:
                finalNums.append(x)
        k = len(finalNums)
        
        return k

obj = Solution

obj.removeDuplicates([1,1,2])