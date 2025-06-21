class Solution {
public:
    int minimumDeletions(string word, int k) {
       unordered_map<char,int> mp;
       for(auto w : word )
       {
         mp[w]++;
       }
       int ans = word.length();
       for(auto &[_,a] : mp)
       {
         int del = 0;
         for(auto &[_,b]: mp)
         {      
            if(b<a)
               del += b;
            else if(b> a+k)
               del += (b-(a+k));     
         }
         ans = min(ans,del);
       }
        return ans;

    }
};