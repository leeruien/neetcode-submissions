# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        count_r = self.maxDepth(root.left)
        count_l = self.maxDepth(root.right)
        return max(count_r,count_l) +1

        