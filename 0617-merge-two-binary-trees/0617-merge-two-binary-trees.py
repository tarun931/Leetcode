# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root1 , root2):
            if not root1 and not root2:
                return None
            val = 0    
            if root1 and not root2 :
                val = root1.val
            elif root2 and not root1:
                val = root2.val
            else:
                val = root1.val+root2.val    
            root = TreeNode(val)
            root.left = helper(root1.left if root1 else None , root2.left if root2 else None)    
            root.right = helper(root1.right if root1 else None , root2.right if root2 else None)      
            return root 

        return helper(root1 , root2)           


        