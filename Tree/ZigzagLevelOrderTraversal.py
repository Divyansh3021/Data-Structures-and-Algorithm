# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        left_to_right = True

        q = collections.deque()
        q.append(root)

        while q:
            lvl_list = []

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    lvl_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if lvl_list:
                if not left_to_right:
                    lvl_list.reverse()
                    left_to_right = True
                else:
                    left_to_right = False
                res.append(lvl_list)

        return res
