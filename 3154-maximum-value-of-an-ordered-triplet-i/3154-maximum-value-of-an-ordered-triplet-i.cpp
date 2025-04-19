class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long int res = 0;
        long long int maxi = 0;
        long long int diff_maxi = 0 ;
        for(int k=0;k<nums.size();k++)
        {
           res = max(res,diff_maxi*(1LL*nums[k]));
           diff_maxi = max(diff_maxi , maxi-(1LL*nums[k]));
           maxi = max(maxi,1LL*nums[k]);
           
        }
        return res;
    }
};