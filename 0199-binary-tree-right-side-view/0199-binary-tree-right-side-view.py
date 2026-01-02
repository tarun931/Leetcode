# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if not root:
                return []
            res = []    
            q = deque()
            q.append(root)
            while q :
                rtnode = None
                l = len(q)
                for i in range(l):
                    node = q.popleft() 
                    if node :
                        rtnode = node
                        q.append(node.left)
                        q.append(node.right)
                if rtnode:        
                    res.append(rtnode.val)   
            return res
        return helper(root)        




        