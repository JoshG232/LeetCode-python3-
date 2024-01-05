class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
        


obj = Solution()

obj.invertTree([1,2,3])