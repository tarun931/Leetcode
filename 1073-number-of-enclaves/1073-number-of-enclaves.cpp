class Solution {
public:
    int dfs(int i, int j ,int row, int col,vector<vector<int>>& grid,vector<vector<int>>& vis)
    {
        if(i<0 || j<0 || i==row||j==col || grid[i][j]==0 || vis[i][j]==1)
        {
            return 0;
        }
        vis[i][j]=1;
        int cnt =1 ;
        cnt += dfs(i+1,j,row,col,grid,vis)+dfs(i-1,j,row,col,grid,vis)+dfs(i,j+1,row,col,grid,vis)+dfs(i,j-1,row,col,grid,vis);
        return cnt;
    }
    int numEnclaves(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        int land =0;
        int bland =0;
        vector<vector<int>> vis(row,vector<int>(col,0));
        for(int i=0;i<row;i++)
        {
            for(int j =0;j<col;j++)
            {
                if(grid[i][j])
                    land++;   
                if(!vis[i][j] && grid[i][j]==1 && (i==0 || j==0 || i==row-1 || j==col-1))
                {
                   bland+= dfs(i,j,row,col,grid,vis);
                }
            }
        }
        return land-bland;
    }
};