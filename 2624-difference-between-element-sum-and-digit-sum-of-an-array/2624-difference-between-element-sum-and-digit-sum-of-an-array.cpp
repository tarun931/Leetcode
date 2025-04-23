class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int digsum=0;
        int elesum=0;
        for(int i=0;i<nums.size();i++)
        {
            elesum+=nums[i];
        }
        for(int i=0;i<nums.size();i++)
        {
            int digi= nums[i];
            while(digi)
            {
                digsum+= digi%10;
                digi= digi/10;
            }
        }
        int ans= digsum-elesum;
        return abs(ans);
    }
};