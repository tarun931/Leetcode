# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root :
                return 0,0
            if not root.left and not root.right :
                return root.val  , root.val  
            left_ans , lefty = helper(root.left)
            right_ans , righty = helper(root.right)
            lefty = max(lefty, 0)
            righty = max(righty ,0)
            maxi = max(lefty + root.val+righty , left_ans, right_ans)
            return maxi , max(lefty ,righty)+root.val    

        ans , _ = helper(root)
        return ans
             
        