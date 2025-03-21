# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        def presearch(node, depth):
            if not node:
                return
            
            if depth == len(result):
                result.append(node.val)
            else:
                result[depth] = max(result[depth], node.val)
            
            presearch(node.left, depth + 1)
            presearch(node.right, depth + 1)

        result = []
        presearch(root, 0)
        return result