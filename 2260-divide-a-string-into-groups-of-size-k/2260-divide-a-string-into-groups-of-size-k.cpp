class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans ;
        string sol = "";
        for(int i=0;i<s.length();i++)
        {
            if(sol.size()==k)
            {
                ans.push_back(sol);
                sol.clear();
            }
            sol += s[i];
        }
        ans.push_back(sol);
        int n = ans.size();
        int m = ans[n-1].size();
        if(m<k)
        {
            while(m<k)
            {
                ans[n-1] += fill ;
                m = ans[n-1].size();
            }
        }
        return ans;
    }
};