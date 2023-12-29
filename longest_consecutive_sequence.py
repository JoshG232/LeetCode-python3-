from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(dict.fromkeys(nums))
        print(nums)
        longest = 0
        tempCount = 0
        if len(nums) == 0:
            return 0
        for x in range(len(nums)-1):
            print(nums[x], " and ", nums[x+1])
            if nums[x]+1 == nums[x+1]:
                tempCount = tempCount + 1
                if tempCount > longest:
                    longest = longest + 1
            else:
                tempCount = 0
        print("Longest: " ,longest+1)



obj = Solution()

obj.longestConsecutive([1,2,0,1])