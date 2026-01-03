# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [] 
        def helper(root):
            if not root :
                return []
            q = deque()
            q.append(root)
            while q:
                res = []
                l = len(q)
                for i in range (0,l):
                    cur = q.popleft()
                    if cur:
                        res.append(cur.val)
                        if cur.left:
                            q.append(cur.left)
                        if cur.right:
                            q.append(cur.right)
                ans.append(res) 
           
        helper(root)
        return ans               


                
                
                
                
                


        