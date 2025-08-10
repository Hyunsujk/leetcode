# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []

        def inorder(node):
            if not node:
                return None

            left = inorder(node.left)
            if left is not None:
                return left
            
            visited.append(node.val)
            if len(visited) == k:
                return node.val
            
            return inorder(node.right)
        
        return inorder(root)
        