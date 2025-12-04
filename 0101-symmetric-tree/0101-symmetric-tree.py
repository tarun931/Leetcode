# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(p,q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if  p.val == q.val:
                return sym(p.left,q.right) and sym(p.right , q.left)
            return False    
        if not root:
            return True
        return sym(root.left , root.right)


        