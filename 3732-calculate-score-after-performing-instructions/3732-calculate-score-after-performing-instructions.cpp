class Solution {
public:
    long long calculateScore(vector<string>& ins, vector<int>& v) {
        vector<int> vis(v.size(),0);
        int i=0;
        long long int cnt = 0 ;
            while( i>=0 && i<vis.size() && (vis[i]!=1))
            {
                vis[i]=1;
                if(ins[i][0]=='j'){
                     i = i + v[i];
                }    
                else
                {
                    cnt = cnt + v[i];
                    i++;
                }
                
            }
        return cnt ; 
    }
};