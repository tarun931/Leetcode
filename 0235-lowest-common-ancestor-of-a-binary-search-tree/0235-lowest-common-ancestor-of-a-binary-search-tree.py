# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q :
            return root
        maxi, minin = p.val , p.val    
        maxi , mini = max(p.val , q.val) , min(p.val , q.val)    
        if (maxi>= root.val and mini<=root.val):
            return root    
        return   self.lowestCommonAncestor(root.left , p,q) or  self.lowestCommonAncestor(root.right , p, q) 


        