# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(node):
            if not node:
                return True , 0
            lefty , hl = bal(node.left)
            righty , hr = bal(node.right)
            if (not lefty) or (not righty) or abs(hl-hr)>1 : 
                return False,0
            return True,max(hl , hr)+1
        ans , _ = bal(root)  
        return ans          
                


        