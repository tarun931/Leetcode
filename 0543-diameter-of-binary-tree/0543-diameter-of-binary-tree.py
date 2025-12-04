# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def d(node,h):
            if not node:
                return 0,0
            lefty,lh = d(node.left,h+1)
            righty,rh =d(node.right,h+1)
            cur = lh + rh
            ht = max(lh , rh)+1
            return max(lefty , righty , cur) , ht
        ans,x = d(root,0)
        return ans    





        