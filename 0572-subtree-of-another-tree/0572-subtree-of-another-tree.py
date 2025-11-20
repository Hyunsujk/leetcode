# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_path = self.preorder(root)
        subRoot_path = self.preorder(subRoot)

        return subRoot_path in root_path

    def preorder(self, node):
        if not node:
            return "N"
        path = ""
        path += "," + str(node.val) + ","
        path += self.preorder(node.left)
        path += self.preorder(node.right)
        return path
        