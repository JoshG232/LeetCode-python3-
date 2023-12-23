from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countDict = defaultdict(list)
        for x in nums:
            countDict[x].append(x)

        # print(countDict.values())

        finalDict = {}
        for j in countDict:
            print("Value: ", countDict[j][0])
            print("Length: " , len(countDict[j]))
            finalDict[countDict[j][0]] = len(countDict[j])

        print(finalDict)
        finalArr = []
        for number in range(k):
            highestValue = max(finalDict, key=finalDict.get)
            # print(highestValue)
            finalArr.append(highestValue)
            finalDict.pop(highestValue)

        print(finalArr)
        return finalArr

obj = Solution()

obj.topKFrequent([1,1,1,2,2,4],2)