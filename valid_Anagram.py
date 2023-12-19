class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        arrS = list(s)
        arrS.sort()
        arrT = list(t)
        arrT.sort()

        if (arrS == arrT):
            return True
        else:
            return False
        


obj1 = Solution()

obj1.isAnagram("Hello","olldasdeH")