class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int: 
        g = [[] for _ in range(n)]
        for u , v in edges:
            g[u].append(v)
            g[v].append(u)

        root = 0
        
        def helper(node , parent):
            total_components = 0
            rem_sum = values[node]% k 
            for child in g[node]:
                if parent == child:
                    continue
                child_components , child_rem  = helper(child , node)
                total_components += child_components
                if child_rem == 0 :
                    total_components += 1
                else:
                    rem_sum = (rem_sum+child_rem)%k  
            return total_components , rem_sum   

        total_components , rem_sum = helper(root , -1)

        if rem_sum == 0:
            total_components+=1
        return total_components    




        