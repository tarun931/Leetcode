class Solution {
public:
    // vector<int> buildArray(vector<int>& nums) {
    //     vector<int> ans;
    //     for(int i=0;i<nums.size();i++)
    //         ans.push_back(nums[nums[i]]);
    //     return ans;
    // }
    //inplace 
    vector<int> buildArray(vector<int>& nums) {
        //build array to store both original value(%1000) and final value(when divide by /1000) ,since values only range from [0,999]
        for(int i=0;i<nums.size();i++)
            nums[i] = nums[i] + 1000*(nums[nums[i]] % 1000); 
        
        // get values

        for(int i=0;i<nums.size();i++)
        {
            nums[i] = nums[i]/1000 ;
        }
        return nums;
    }
};