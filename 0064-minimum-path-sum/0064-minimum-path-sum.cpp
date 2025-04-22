class Solution {
public:
    int helper(vector<vector<int>>& grid)
    {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> dp(n,vector<int>(m,0));
        dp[0][0] = grid[0][0];
        for(int i=1;i<n;i++)
             dp[i][0] = dp[i-1][0] + grid[i][0]; 
           
        for(int i=1;i<m;i++)
             dp[0][i] = dp[0][i-1] + grid[0][i];

        for(int i=1;i<n;i++)
        {
            for(int j=1;j<m;j++)
            {
                dp[i][j] = grid[i][j]+min(dp[i-1][j],dp[i][j-1]);
            }
        }   
        return dp[n-1][m-1];
    }
    int helper2(vector<vector<int>>& grid)
    {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> prev(m,0),cur(m,0);
        prev[0] = grid[0][0];
        for(int i=1;i<m;i++)
             prev[i] = prev[i-1] + grid[0][i]; 
           
        for(int i=1;i<n;i++)
        {
            cur[0] = prev[0] + grid[i][0];
            for(int j=1;j<m;j++)
            {
                cur[j] = grid[i][j]+min(prev[j],cur[j-1]);
            }
            prev = cur ;
        }   
        return prev[m-1];
    }
    int minPathSum(vector<vector<int>>& grid) {
        return helper2(grid);
    }
};