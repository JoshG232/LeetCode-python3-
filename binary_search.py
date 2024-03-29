from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[l] != target:
            print("not found")
            return -1
        print("Found")
        return l





obj = Solution()

obj.search([-1,0,3,5,9,12],5)