# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    p = "->".join(map(str,path))
                    paths.append(p)
                else:
                    dfs(node.left, path)
                    dfs(node.right, path)
                path.pop()
        
        dfs(root, [])
        return paths
        