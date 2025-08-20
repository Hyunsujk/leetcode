# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        while not root:
            return 0

        queue = [root]
        level = 0

        new_level = []
        while queue:
            node = queue.pop()
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
            
            if not queue:
                level += 1
                queue = new_level
                new_level = []

        
        return level


        