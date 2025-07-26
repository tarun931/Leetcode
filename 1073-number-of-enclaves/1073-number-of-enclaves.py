class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row,col = len(grid) , len(grid[0])
        vis = set()
        land, bland = 0,0
        
        def dfs(i,j):
            if i < 0 or j<0 or i==row or j==col or (i,j) in vis or grid[i][j] == 0:
                return 0
            cnt = 1    
            vis.add((i,j))
            cnt += dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            return cnt

        for i in range(row):
            for j in range(col):
                land += grid[i][j]
                if grid[i][j]==1 and (i,j) not in vis and (i in [0,row-1] or j in [0,col-1]):
                    bland += dfs(i,j)


        return land - bland 
        