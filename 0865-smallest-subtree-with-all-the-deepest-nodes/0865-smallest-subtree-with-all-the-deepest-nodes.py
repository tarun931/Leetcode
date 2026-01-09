# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.parent = {} 
        # self.ans = []
        # self.parent[root] = None
        # def helper(root):
        #     q = deque()
        #     q.append(root)
        #     while q:
        #         l = len(q)
        #         res = []
        #         for i in range(l):
        #             cur = q.popleft()
        #             if cur :
        #                 if cur.left:
        #                 q.append(cur.left)
        #                 self.parent[cur.left] = cur
        #                 if cur.right:
        #                     q.append(cur.right)
        #                     self.parent[cur.right] = cur
        #             res.append(cur)
        #         self.ans.append(res)
        #     return 
        # helper(root)
        # res = self.ans.pop()
        # sol = set()
        # l = len(res)
        # if res[0] == root:
        #     return root
        # i = 0    
        # self.p = set()
        # while len(self.p)>1 or i==0 :
        #     i+=1
        #     if i != 0:
        #         res[:] = self.p
        #     self.p.clear()
        #     for ele in res:
        #         self.p = self.parent[ele]

        # return self.p.pop()    
        parent = {root: None}

        # BFS
        q = deque([root])
        last_level = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node)

                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)

            last_level = level  

        # Start from deepest nodes
        curr = set(last_level)

        # Climb parents until one node remains
        while len(curr) > 1:
            curr = set(parent[node] for node in curr)

        return curr.pop()
   
            
    

                



                        







        