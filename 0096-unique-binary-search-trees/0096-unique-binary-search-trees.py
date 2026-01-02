class Solution:
    def numTrees(self, n: int) -> int:
        def helper(n):
            num = [1]*(n+1)
            for nodes in range(2,n+1):
                total = 0
                for root in range(1,nodes+1):
                    left =  root-1
                    right = nodes-root
                    total += num[left]*num[right]
                num[nodes] = total

            return num[n]
        return helper(n)        

            
                
                    
        