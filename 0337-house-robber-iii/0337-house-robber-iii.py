# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root :
                return 0, 0
            wl , wtl = helper(root.left)
            wr , wtr = helper(root.right)

            return wtl+wtr+root.val , max(wl,wtl)+max(wr,wtr)
        maxi1 , maxi2 = helper(root)
        return max(maxi1, maxi2)         

        