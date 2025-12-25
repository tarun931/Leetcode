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
            if root1 and root2:
                root.left = helper(root1.left , root2.left)
            elif root1:
                root.left = helper(root1.left , None)
            elif root2:
                root.left = helper(None , root2.left)
            else:
                root.left = None    

            if root1 and root2:        
                root.right = helper(root1.right , root2.right)
            elif root1:
                root.right = helper(root1.right , None)
            elif root2:
                root.right = helper(None , root2.right)   
            else:
                root.right = None         
            return root 

        return helper(root1 , root2)           


        