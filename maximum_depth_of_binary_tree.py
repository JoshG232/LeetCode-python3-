"""
Bit of a fail to write. But using max to understand the depth with adding 1 each return to get to a none type so that it will find the max depth in each branch
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        depth = 1
        tempDepth = 1
        print(root.val)
        print("Depth: ", depth)

        if root.left is not None:
            tempDepth = tempDepth + 1
            if tempDepth > depth:
                depth = tempDepth
            self.maxDepth(root.left)
            tempDepth = 1
        if root.right is not None:
            tempDepth = tempDepth + 1
            if tempDepth > depth:
                depth = tempDepth
            self.maxDepth(root.right)
            tempDepth = 1




obj = Solution()

obj.maxDepth([3,9,20,None,None,15,7])