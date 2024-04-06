from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        splitElements = defaultdict(list)
        for x in nums:
            print(x)
            splitElements[x].append(x)
    
        print(splitElements)

        print(max(splitElements.values(), key=len)[0])

        return max(splitElements.values(), key=len)[0]

obj = Solution()

obj.majorityElement([3,2,3]) 