# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return True , 0
            lefty , hl = helper(root.left)
            if not lefty:
                return False , 0
            righty , rl = helper(root.right)    
            if not righty or abs(rl-hl)>1 :
                return False , 0
            return True , max(rl , hl)+1
        ans , _ = helper(root)
        return ans         

            



                


        