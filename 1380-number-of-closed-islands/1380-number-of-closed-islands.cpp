class Solution {
public:
    int dfs(int i , int j,int row,int col,vector<vector<int>>& grid,vector<vector<bool>>& vis)
    {
       if(i<0 || j<0 || i==row || j==col)
            return 0;
       if(grid[i][j]==true || vis[i][j])
            return 1;
       vis[i][j] = true;
       return min(dfs(i+1,j,row,col,grid,vis),min(dfs(i-1,j,row,col,grid,vis),min(dfs(i,j+1,row,col,grid,vis),dfs(i,j-1,row,col,grid,vis))));          
    }
    int closedIsland(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        int ans = 0;
        vector<vector<bool>> vis(row,vector<bool>(col));
        for(int i=0;i<row;i++)
        {
            for(int j =0;j<col;j++)
            {
                if(grid[i][j]==0 && vis[i][j]==false)
                { 
                    ans += dfs(i,j,row,col,grid,vis);
                }
            }
        }
        return ans;
    }
};