# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}
        self.root_idx = 0

        def helper(start,end):
            if start > end:
                return None
            
            root_val = preorder[self.root_idx]
            self.root_idx += 1
            root_node = TreeNode(root_val)

            root_inorder_idx = index_map[root_val]
            root_node.left = helper(start, root_inorder_idx - 1)
            root_node.right = helper(root_inorder_idx+1, end)

            return root_node
        
        return helper(0, len(inorder)-1)
