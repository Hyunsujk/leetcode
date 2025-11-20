# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.preorder_idx = 0

        def helper(start, end):
            if start > end:
                return
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            root_node = TreeNode(root_val)
            root_inorder_idx = inorder_idx[root_val]
            root_node.left = helper(start, root_inorder_idx - 1)
            root_node.right = helper(root_inorder_idx + 1, end)

            return root_node
        
        return helper(0, len(inorder)-1)


        