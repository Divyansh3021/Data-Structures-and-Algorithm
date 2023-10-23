# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #do a BFS
        result = []

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
                result.append(lvl_list)
        
        return result