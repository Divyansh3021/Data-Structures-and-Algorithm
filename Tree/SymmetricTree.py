# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()

        q.append(root.left)
        q.append(root.right)

        while q: 
            lvl_list = []
            for i in range(len(q)):
                node = q.popleft()
                lvl_list.append(node.val) if node else lvl_list.append(None)
                if node:
                    q.append(node.left)
                    q.append(node.right)
            
            mid = len(lvl_list)//2
            # print("Current Lvl_list: ",lvl_list)
            # print("Lists are: ", lvl_list[:mid], "and ",lvl_list[-1:mid-1:-1])
            if lvl_list[:mid] != lvl_list[-1:mid-1:-1]:
                return False
        return True