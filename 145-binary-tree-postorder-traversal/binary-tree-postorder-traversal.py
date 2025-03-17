# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # recurse

        def preorder(node):

            if node:
                preorder(node.left)

            
                preorder(node.right)
                
                ans.append(node.val)


        preorder(root)
        return ans
