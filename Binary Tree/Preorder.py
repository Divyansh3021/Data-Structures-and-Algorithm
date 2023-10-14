# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #Iterative Traversal
        res = []
        cur = root
        stack = []

        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        
        return res

        #Recursive Traversal

        # def preorder(cur):
        #     if not cur:
        #         return
        #     res.append(cur.val)
        #     preorder(cur.left)
        #     preorder(cur.right)

        # preorder(cur)
        # return res