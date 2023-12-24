from typing import List
from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrProductNums = []
        for x in nums:
            product = x
            

            for i in nums:
                if (i == x):
                    continue
                product = product * i
            if (product == 0):
                arrProductNums.append(0)
                continue
            product = product / x
            product = int(product)
            arrProductNums.append(product)

        print(arrProductNums)
        return arrProductNums

obj = Solution()

obj.productExceptSelf([-1,1,0,-3,3])