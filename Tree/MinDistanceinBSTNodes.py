# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.res = float("inf")
        self.prev = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.Inorder(root)
        return self.res
    
    def Inorder(self, node):
        if not node:
            return
        
        self.Inorder(node.left)

        if self.prev:
            self.res = min(self.res, node.val - self.prev.val)
        self.prev = node

        self.Inorder(node.right)