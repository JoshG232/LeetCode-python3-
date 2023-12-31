from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = 100000000000000000000000000000000000000000000000000000000000
        for x in range(len(prices)):
            if prices[x] == 10000:
                return 0
            
            if (prices[x] < lowest):
                lowest = prices[x]
            else:
                continue
            for j in range(x+1,len(prices)):
                if (prices[j] - prices[x] > profit):
                    profit = prices[j] - prices[x]
        print(profit)
        return profit


obj = Solution()

obj.maxProfit([2,3,4])