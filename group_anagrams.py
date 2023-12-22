from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for x in strs:
            sortedString = ''.join(sorted(x))
            group[sortedString].append(x)
            
        return list(group.values())



obj = Solution()

obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"])