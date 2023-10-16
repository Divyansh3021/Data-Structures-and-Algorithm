# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth(node):
            if node.left:
                left = depth(node.left)
            else:
                left = 0
            
            if node.right:
                right = depth(node.right)
            else:
                right = 0
            
            if left + right > self.diameter:
                self.diameter = left + right
            
            return  1 + max(left,right)
        
        depth(root)
        return self.diameter