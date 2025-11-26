class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9+7
        m = len(grid)
        n = len(grid[0])
        dp = [[[0]* k for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    dp[i][j][grid[0][0]%k] = 1
                    continue
                value = grid[i-1][j-1]% k 
                for r in range(k):
                    prev_mod = (r-value+k)%k
                    dp[i][j][r]=(dp[i-1][j][prev_mod]+dp[i][j-1][prev_mod])%MOD

        return dp[m][n][0]                



'''

   3d because , I want to store , in how many ways I can reach that cell , and remainder of each way . In total there will be 0 to (k-1) remainders possible thats why m*n*k .
   
   dp[0][0]  = 1 , (How many ways can I reach at this cell with diff sums -> only 1) 

'''     