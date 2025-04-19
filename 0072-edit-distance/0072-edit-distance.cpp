class Solution {
public:
    // int helper(string word1, string word2,int i ,int j)
    // {
    //     if(i==word1.length())
    //          return word2.length()-j;          
    //     if(j==word2.length())
    //          return word1.length()-i;     
    //     int one = INT_MAX;
    //     int two = INT_MAX;
    //     int three = INT_MAX;
    //     int four = INT_MAX;
    //     if(word1[i]==word2[j])
    //         one  =  helper(word1,word2,i+1,j+1);
    //     else {
    //         two = 1 + helper(word1,word2,i+1,j);
    //         three = 1+ helper(word1,word2,i,j+1);
    //         four = 1 + helper(word1,word2,i+1,j+1);
    //     }    
    //     return min(one, min(two,min(three,four)));
    // }
    int helper(string word1, string word2)
    {
        int n = word1.length();
        int m = word2.length();
        vector<vector<int>> dp(n+1,vector<int>(m+1,0));
        for(int i=0;i<=n;i++)
        {
            for(int j = 0;j<=m ;j++)
            {
                if(i==0)
                   dp[i][j] = j ; 
                else if(j==0)
                   dp[i][j] = i;   
                else if(word1[i-1]==word2[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else
                {
                    dp[i][j] = 1 + min(dp[i-1][j],min(dp[i][j-1],dp[i-1][j-1]));
                }    
            }
        }
        return dp[n][m];
    }
    int minDistance(string word1, string word2) {
        return helper(word1,word2);
    }
};