class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int,int> mp ;
        for(int i=0;i< answers.size();i++)
        {
            mp[answers[i]] += 1;
        }
        int cnt = 0 ;
        for(auto it : mp)
        {
            cnt += ceil((double)it.second / (it.first+1)) * (it.first+1) ;
        }
        return cnt;
    }
};