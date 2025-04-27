class Solution {
public:
    int countSubarrays(vector<int>& nums) {
       int cnt = 0;
       for(int i=2;i<nums.size();i++)
       {
         float one = nums[i-2];
         float two = nums[i-1];
         float th = nums[i];
         if((two/2)==(one+th))
            cnt++;
       }
       return cnt ;
    }
};