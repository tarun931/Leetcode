class Solution {
public:
     int helper(vector<int>& nums,int ind)
    {
        if(ind>=nums.size())
             return 0 ;
        int take = nums[ind] + helper(nums,ind+2);        
        int skip = helper(nums,ind+1) ;      
        return max(take , skip) ;
    }
    int helper2(vector<int>& nums)
    {   int n = nums.size();
        vector<int> dp(n+1,0);
        dp[0] = 0;
        dp[1] = nums[0];
        for(int i=2;i<=n;i++)
        {
            dp[i] = max(dp[i-1] , dp[i-2] + nums[i-1]);
        }
        return dp[n];
    }
    int rob(vector<int>& nums) {
        if(nums.size()==1)
             return nums[0];
        if(nums.size()==2)
             return max(nums[0],nums[1]);          
         return helper2(nums);
         
    }
};