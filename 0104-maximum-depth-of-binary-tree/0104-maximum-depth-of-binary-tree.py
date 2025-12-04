# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ans = 0 
        def ht(node):
            if not node:
                return 0
            lefty = ht(node.left)
            righty = ht(node.right)
            maxi = max(lefty,righty)
            return maxi+1
        ans  = ht(root)    
        return ans    



        