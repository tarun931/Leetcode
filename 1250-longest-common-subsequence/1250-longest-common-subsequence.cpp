class Solution {
public:
    int helper(string t1, string t2,int i, int j)
    {
         if(i>= t1.length() || j>= t2.length())
              return 0;
         if(t1[i] == t2[j])
            return 1 + helper(t1,t2 ,i+1,j+1);
        return  max(helper(t1,t2,i+1,j),helper(t1,t2,i,j+1));            
    }
    int helper2(string t1, string t2)
    {
        int n = t1.length();
        int m = t2.length();
        vector<vector<int>> dp(n+1,vector<int>(m+1,0));
        for(int i=1;i<=n ;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(t1[i-1]==t2[j-1])
                    dp[i][j] = 1 + dp[i-1][j-1];
                else
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
        return dp[n][m];
    }
    int helper3(string t1, string t2)
    {
        int n = t1.length();
        int m = t2.length();
        vector<int> prev(m+1,0),cur(m+1,0);
        for(int i=1;i<=n ;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(t1[i-1]==t2[j-1])
                    cur[j] = 1 + prev[j-1];
                else
                    cur[j] = max(prev[j],cur[j-1]);
            }
            prev = cur;
        }
        return prev[m];
    }
    int longestCommonSubsequence(string text1, string text2) {
        return helper3(text1,text2);
    }
};
