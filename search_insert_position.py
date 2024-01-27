from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for x in nums:
            if x == target or x > target:
                print(count)
                return count
            count += 1

obj = Solution()

obj.searchInsert([1,3,5,6],1)