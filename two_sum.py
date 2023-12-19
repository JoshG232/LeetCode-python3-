from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLength = len(nums)

        for x in range(numsLength):
            for i in range(numsLength):
                if (x == i):
                    continue
                if (nums[x] + nums[i] == target):
                    print("Yaa: ", nums[x], " ", nums[i])
                    return [x,i]




obj = Solution()

obj.twoSum([3,2,4],6)