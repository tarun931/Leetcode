# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0,0
            lft , lfth = helper(root.left)
            rgt , rgth = helper(root.right)

            dia = max(lfth +rgth, rgt, lft) 
            return dia , max(lfth , rgth)+1
        ans , _ = helper(root)
        return ans          





        