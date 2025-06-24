class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        vector<vector<int>> ans;
        vector<int> sol;
        sort(nums.begin(), nums.end());
        int diff = 0;
        int lowest = INT_MAX;
        for (int i = 0; i < nums.size(); i++) 
        {
            if(i==0)
                lowest = nums[0];
            if (i != 0 && sol.size() > 0 && nums[i] - lowest > k) 
            {
                return {};
            }
            if ((i + 1) % 3 == 0 && i != 0) 
            {
                diff = 0;
                sol.push_back(nums[i]);
                ans.push_back(sol);
                sol.clear();
                lowest = INT_MAX;
            } 
            else {
                sol.push_back(nums[i]);
                lowest = min(lowest,nums[i]);
            }
        }
        return ans;
    }
};