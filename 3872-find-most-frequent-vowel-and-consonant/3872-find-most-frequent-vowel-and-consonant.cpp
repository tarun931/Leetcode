class Solution {
public:
    
    int maxFreqSum(string s) {
        //97 to 122
        int vow = 0;
        int cons = 0 ;
        unordered_map<char,int> v;
        unordered_map<char,int> c;
        for(int i=0;i<s.length();i++)
            {
                if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'){
                    v[s[i]]++;
                    int temp = v[s[i]];
                    if(temp>vow)
                        vow=temp;
                }
                       
                else if(s[i]>=97 && s[i]<=122)
                    c[s[i]]++;
                    int temp = c[s[i]];
                    if(temp>cons)
                        cons=temp;
            }
        return cons+vow;
        
    }
};