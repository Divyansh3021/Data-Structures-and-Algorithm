# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #right most element of the level traversal in BFS

        res = []
        
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
                res.append(lvl_list[-1])

        return res