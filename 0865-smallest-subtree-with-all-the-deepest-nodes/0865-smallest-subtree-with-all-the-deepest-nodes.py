# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:    
#         parent = {root: None}

#         # BFS
#         q = deque([root])
#         last_level = []

#         while q:
#             level = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 level.append(node)

#                 if node.left:
#                     parent[node.left] = node
#                     q.append(node.left)
#                 if node.right:
#                     parent[node.right] = node
#                     q.append(node.right)

#             last_level = level  

#         # Start from deepest nodes
#         curr = set(last_level)

#         # Climb parents until one node remains
#         while len(curr) > 1:
#             curr = set(parent[node] for node in curr)

#         return curr.pop()
   
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:    
        def dfs(node):
            if not node:
                return (0, None)
            ld, lnode = dfs(node.left)
            rd, rnode = dfs(node.right)

            if ld > rd:
                return (ld + 1, lnode)
            if rd > ld:
                return (rd + 1, rnode)

            return (ld + 1, node)

        return dfs(root)[1]

   
                        
    

                



                        







        