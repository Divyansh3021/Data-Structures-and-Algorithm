#-----problem no. 652-----


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)

        def preOrder(node):
            if not node:
                return "null"
            
            s = ",".join([str(node.val), preOrder(node.left), preOrder(node.right)])

            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s
        
        res = []
        preOrder(root)
        return res