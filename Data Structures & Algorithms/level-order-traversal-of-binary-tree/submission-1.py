# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = [[root.val]]
        while True:
            current_level = []
            current_level_val = []
            while queue:
                cur = queue.pop(0)
                if cur.left: 
                    current_level.append(cur.left)
                    current_level_val.append(cur.left.val)
                if cur.right: 
                    current_level.append(cur.right)
                    current_level_val.append(cur.right.val)
            if current_level == []: break
            queue = current_level
            res.append(current_level_val)
        return res

            
