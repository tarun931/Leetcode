class Solution {
public:
    int numTilings(int n) {
        int mod= 1000000007;
        if(n==1)
           return 1;
        if(n==2)
            return 2;
        if(n==3)
            return 5;
        //int ans = 2*numTilings(n-1) + numTilings(n-3) ; 
        vector<long long int> dp(n+1);
        dp[0]=0;
        dp[1]=1;
        dp[2]=2;
        dp[3]=5;
        for(int i=4;i<=n;i++)
        {
           dp[i]= ((2*(1LL*dp[i-1]%mod))%mod + dp[i-3]%mod)%mod;
        }
        return dp[n]%mod;     
    }
};