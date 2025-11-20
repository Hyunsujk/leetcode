# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        left_n =  self.invertTree(root.right)
        right_n = self.invertTree(root.left)
        root.left = left_n
        root.right = right_n
        return root
        
        