class Solution {
public:
    int helper(int m , int n )
    {
        vector<vector<int>> dp(m,vector<int>(n,0));
        for(int i=0;i<m;i++)
            dp[i][0]=1;
        for(int i=0;i<n;i++)
            dp[0][i] = 1;
        for(int i=1;i<m;i++)
        {
            for(int j = 1;j<n;j++)
            {
                dp[i][j] = dp[i-1][j]+dp[i][j-1];    
            }
        }
        return dp[m-1][n-1] ;
    }
    int helper2(int m , int n )
    {
        vector<int> prev(n,1),cur(n,0);
        // for(int i=0;i<m;i++);
        //     dp[i][0]=1;
        // for(int i=0;i<n;i++)
        //     dp[0][i] = 1;
        for(int i=1;i<m;i++)
        {
            prev[0]=1;
            cur[0]=1;
            for(int j = 1;j<n;j++)
            {
                cur[j] = prev[j]+cur[j-1];    
            }
            prev=cur;
        }
        return prev[n-1];
    }
    int uniquePaths(int m, int n) {
        return helper2(m,n);
    }
};