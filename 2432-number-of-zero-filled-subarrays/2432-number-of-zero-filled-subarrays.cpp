class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        
        long long int ans=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]!=0)
              continue;
            long long int res =0;
            long long int len =0;
            
                res=1;
                 len=1;
                 i++;
                while(i<nums.size() && nums[i]==0)
                {
                   len = len + 1;
                   res +=len;
                   i++;
                }
            
            ans += res;
        }
        return ans;
    }
};