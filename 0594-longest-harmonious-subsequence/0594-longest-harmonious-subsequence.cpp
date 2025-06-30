class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int,int>mp;
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        if(mp.size()==1)
           return 0;
        int ans=0;
        for(auto x: mp)
        { 
            
          if(x.second>0 && mp[x.first+1]){
              ans = max(ans,x.second+mp[x.first+1]);
              cout<< x.first<<endl;
              }
        }
        return ans;
    }
};