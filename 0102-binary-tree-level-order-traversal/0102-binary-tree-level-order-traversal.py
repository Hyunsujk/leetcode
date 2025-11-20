# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            curr_val = []
            next_level = []
            for n in q:
                curr_val.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            q = next_level
            res.append(curr_val)
        return res
        
                

        