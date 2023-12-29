class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        reverse = str(x)[::-1]
        if int(reverse) == x:
            return True
        else: 
            return False




obj = Solution()

obj.isPalindrome(323)