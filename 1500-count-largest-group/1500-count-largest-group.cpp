class Solution {
public:
    int countLargestGroup(int n) {
        unordered_map<int,int> mp;
        for(int i=1;i<=n;i++)
        {
           string str = to_string(i);
           int digit =0 ;
           for(int j=0;j<str.length();j++)
           {
             digit = digit + (str[j] - '0');
           } 
           mp[digit] +=1 ;
        }
        int ans = 0;
        int size = 0;
        for(auto it : mp)
        {
          size = max(size,it.second);
        }
        for(auto it : mp)
        {
            if(it.second == size )
                 ans++;
        }
        return ans;
    }
};