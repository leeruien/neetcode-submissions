# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check which side 
        root_val = root.val
        if p.val > root_val and q.val > root_val:
            node = self.lowestCommonAncestor(root.right,p,q)
        elif p.val < root_val and q.val < root_val:
            node = self.lowestCommonAncestor(root.left,p,q)
        else: return root
        return node



