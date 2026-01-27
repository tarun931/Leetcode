class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        INF = float('inf')
        graph = [[] for _ in range(n)]
        
        for from_node, to_node, cost in edges:
            graph[from_node].append((to_node, cost))
            graph[to_node].append((from_node, cost * 2))
        
        d = [INF] * n
        d[0] = 0
        q = [(0, 0)]
        
        while q:
            distance, from_node = heappop(q)
            if distance > d[from_node]:
                continue
            
            for to_node, cost in graph[from_node]:
                if d[to_node] > d[from_node] + cost:
                    d[to_node] = d[from_node] + cost
                    heappush(q, (d[to_node], to_node))
        
        return -1 if d[n - 1] == INF else d[n - 1]