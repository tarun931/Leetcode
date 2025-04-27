class Solution {
public:
    int countSubarrays(vector<int>& nums) {
    //    int one = nums[0];
    //    int two = nums[1];
    //    int th = nums[2];
       int cnt = 0;
    //    if((th/2)==(one+two))
    //         cnt++;
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