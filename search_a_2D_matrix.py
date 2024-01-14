from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for x in matrix:
            print(x)
            if target >= x[0] and target <= x[-1]:
                nums = x[::]
                l = 0
                r = len(nums) - 1

                while l < r:
                    mid = l + (r - l) // 2
                    if nums[mid] >= target:
                        r = mid
                    else:
                        l = mid + 1

                if nums[l] != target:
                    return False
                return True



obj = Solution()

obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
