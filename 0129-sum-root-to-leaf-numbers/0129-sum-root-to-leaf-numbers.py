# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root , ans):
            if not root:
                return 0     
            ans = ans*10 + root.val
            if not (root.left or root.right):
                return ans 
            anslf = helper(root.left ,ans)    
            ansrt = helper(root.right , ans)
            return anslf+ansrt
        return helper(root , 0) 