class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
           int n = nums.size();
           vector<pair<int,int>> pr;
           for(int i=0;i<nums.size();i++)
           {
            pr.push_back({i,nums[i]});
           }        
           sort(pr.begin(),pr.end(), [&](auto x1 ,auto x2){return x1.second>x2.second;});
           sort(pr.begin(),pr.begin()+k);
           vector<int> ans;
           for(int i=0;i<k;i++)
           {
            ans.push_back(pr[i].second);
           }
           return ans;
    }
};