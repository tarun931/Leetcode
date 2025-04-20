class Solution {
public:
    int maximumPossibleSize(vector<int>& nums) {
        int high = 0 ;
        
        int cnt = 0;
        for(int i=0;i<nums.size();i++)
            {
                if(nums[i]>=high)
                {    high = nums[i];
                }
                else
                {
                    cnt++;
                }
            }
        return nums.size()-cnt;
    }
};