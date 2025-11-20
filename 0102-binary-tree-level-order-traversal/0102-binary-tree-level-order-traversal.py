# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        curr = []
        next_level = []
        while q:
            node = q.pop(0)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            curr.append(node.val)
            if not q:
                res.append(curr)
                q = next_level
                curr = []
                next_level = []
        return res


            

        