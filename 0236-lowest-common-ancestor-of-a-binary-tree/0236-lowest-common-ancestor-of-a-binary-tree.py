# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans  = None
        def anc(node , p,q):
            nonlocal ans
            if not node:
                return False , False
            lftp , lftq = anc(node.left,p,q)
            rtp , rtq = anc(node.right,p,q)   
            cp  = lftp or rtp or node==p 
            cq  = lftq or rtq or node==q
            if cp and cq and ans == None :
                ans = node
            return cp,cq
        anc(root , p ,q)
        return ans        

        