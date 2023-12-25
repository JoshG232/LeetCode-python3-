from typing import List
from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrProducts = []
        for x in range(len(nums)):
            tempNums = nums[:]
            tempNums.remove(tempNums[x])
            # print("tempNums: ", tempNums)
            product = 1
            for i in range(len(tempNums)):
                product = product * tempNums[i]

            # print("Product: ", product)
            arrProducts.append(product)
        
        # print(arrProducts)                
        return arrProducts


obj = Solution()

obj.productExceptSelf([1,2,3,4,0])