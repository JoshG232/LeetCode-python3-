import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(cleaned)
        if (cleaned == cleaned[::-1]):
            return True
        else:
            return False
        




obj = Solution()

obj.isPalindrome("ab_a")