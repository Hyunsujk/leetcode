# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node.left and not node.right:
                return depth + 1
            
            depth += 1
            left_height = right_height = depth
            if node.left:
                left_height = dfs(node.left, depth)
            if node.right:
                right_height = dfs(node.right, depth)
            
            return max(left_height, right_height)
        
        if not root:
            return 0
            
        return dfs(root, 0)


        