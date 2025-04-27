class Solution {
public:
    int countSubarrays(vector<int>& nums) {
       int cnt = 0;
       for(int i=2;i<nums.size();i++)
       {
         if(((float)nums[i-1]/2)==((float)nums[i-2]+(float)nums[i]))
            cnt++;
       }
       return cnt ;
    }
};