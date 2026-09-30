# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(r):
        # return depth, max so far
            if not r: return 0
            count_l = dfs(r.left)
            count_r = dfs(r.right)
            self.res = max(self.res, count_l+count_r)
            return max(count_l,count_r) + 1
        dfs(root)
        return self.res

        