# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # mini , maxi = p.val , p.val
        mini, maxi = min(p.val,q.val) , max(p.val,q.val)    
        if root.val >= mini and root.val<=maxi:
            return root
        # if root.val == p or root.val == q:
        #     return root
        return (self.lowestCommonAncestor(root.left,p ,q) or self.lowestCommonAncestor(root.right,p,q))         
        