class Solution {
public:
    string triangleType(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if (nums[0] + nums[1] <= nums[2])
            return "none";
        unordered_map<int, int> mp;
        int maxi = 0;
        for (auto x : nums) {
            mp[x]++;
            if (mp[x] > maxi)
                maxi = mp[x];
        }
        if (maxi == 3)
            return "equilateral";
        else if (maxi == 2)
            return "isosceles";
        return "scalene";
    }
};