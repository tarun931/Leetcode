class Solution {
public:
    int countLargestGroup(int n) {
        //unordered_map<int,int> mp;
        int freq[37]={0};
        int mf = 1;
        int ans=1;
        freq[1]=1;
        for(int i=2;i<=n;i++)
        {
           
           int digit =0 ;
           for(int x=i;x>0; x/=10 )
                digit += x%10;
            freq[digit] +=1 ;
            if(freq[digit]==mf)
               ans++;
            else if(freq[digit]>mf)
            {
                mf = freq[digit];
                ans = 1;
            }   
        }
        return ans;
        // for(int i=1;i<=n;i++)
        // {
        //    string str = to_string(i);
        //    int digit =0 ;
        //    for(int j=0;j<str.length();j++)
        //    {
        //      digit = digit + (str[j] - '0');
        //    } 
        //    mp[digit] +=1 ;
        //    size = max(size,mp[digit]);
        // }
        // for(auto it : mp)
        // {
        //     if(it.second == size )
        //          ans++;
        // }
        // return ans;
    }
};