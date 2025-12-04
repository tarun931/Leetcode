# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # sumi = 0
        def ans(root):
            if not root:
                return float('-inf'),0
            if not root.left and not root.right:
                return root.val , root.val    
            lsum , lcur = ans(root.left)
            rsum , rcur = ans(root.right)
            lcur = max(lcur,0)
            rcur = max(rcur,0)
            cur = max(lcur,rcur)+root.val 
            return max(lsum,rsum ,lcur+rcur+root.val ) , cur
        sumi, _ = ans(root)
        return sumi    
        