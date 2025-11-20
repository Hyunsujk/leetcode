# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = set()
    
        def dfs(node, max_val):
            if not node:
                return 0
            if node.val >= max_val:
                good_nodes.add(node)
            max_val = max(node.val, max_val)
            if node.left:
                dfs(node.left, max_val)
            if node.right:
                dfs(node.right, max_val)
        
        dfs(root, root.val)
        return len(good_nodes)

