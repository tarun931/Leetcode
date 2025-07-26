class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list) # node -> list of neighbours
        for node, nei,dist in roads:
            adj[node].append((nei,dist))
            adj[nei].append((node,dist))

        def dfs(i):
            if i in vis:
                return
            vis.add(i)    
            nonlocal ans    
            for nei,dist in adj[i]:
                ans = min(ans,dist)    
                dfs(nei)

        ans = float("inf")
        vis = set()
        dfs(1)
        return ans        
        