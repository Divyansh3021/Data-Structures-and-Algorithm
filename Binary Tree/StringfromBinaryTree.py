# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def conStr(root):
            if not root:
                return 
            
            res.append("(")
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")
            
            conStr(root.left)
            conStr(root.right)

            res.append(")")

        conStr(root)
        return  "".join(res)[1: -1]