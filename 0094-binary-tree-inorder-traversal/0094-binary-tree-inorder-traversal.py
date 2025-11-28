# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # def helper(node):
        #     if not node:
        #         return 
        #     helper(node.left)
        #     ans.append(node.val)
        #     helper(node.right)    
        #     return 

        # helper(root)
        # return ans

        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)    
            cur = cur.right
        return ans

        


        