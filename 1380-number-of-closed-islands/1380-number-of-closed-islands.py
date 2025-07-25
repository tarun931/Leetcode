class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row , col = len(grid), len(grid[0])
        vis = set()
        ans = 0 
        def dfs(i,j):
            if i<0 or j<0 or i==row or j ==col:
                return 0
            if grid[i][j] == 1 or (i,j) in vis:
                return 1

            vis.add((i,j))
            return min(dfs(i+1,j),dfs(i-1,j),dfs(i,j-1),dfs(i,j+1))       

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and (i,j) not in vis:
                    ans += dfs(i,j)
        return ans                
        