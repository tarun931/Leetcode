# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(root, v):
            if not root:
                return 0
            lefty = helper(root.left , max(v, root.val) )    
            righty = helper(root.right , max(v, root.val) )
            if root.val >= v :
                return 1 + (lefty+righty) 
            
            return (lefty+righty)
        return helper(root , -1000000)            
                
        