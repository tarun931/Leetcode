class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int ans = 0;
         unordered_map<int,int> mp;
         int n = nums.size();
         int j=0;
         unordered_set<int> dist(nums.begin(),nums.end());
         int dis = dist.size();
         for(int i=0;i<n;i++)
         {
            if(i>0)
            {
                int remove = nums[i-1];
                mp[remove]--;
                if(mp[remove]==0)
                     mp.erase(remove);
            }
            while(j<n && mp.size() < dis)
            {
                int add = nums[j];
                mp[add]++;
                j++;
            }
            if(mp.size() == dis)
                ans += (n-j+1);
         }
         return ans;
    }
};