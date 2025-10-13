# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        
        q = [root]
        while q:
            node = q.pop()
            if node.left:
                left_child = node.left
                right_child = node.right
                node.left = right_child
                node.right = left_child
                q.append(left_child)
                q.append(right_child)
        
        return root