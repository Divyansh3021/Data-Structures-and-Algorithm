#-----Problem: 1448------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxVal):
            if not root:
                return 0
            
            res = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)
            res += helper(root.left, maxVal)
            res += helper(root.right, maxVal)

            return res
        return helper(root, root.val)