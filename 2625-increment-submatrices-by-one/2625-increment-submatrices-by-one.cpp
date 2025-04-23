class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        
        vector<vector<int>> mat(n,vector<int>(n,0));
        vector<vector<int>> diff(n,vector<int>(n,0));
        int t= queries.size();
        while(t--)
        {
            // int ro=queries[t][0];
            // int co=queries[t][1];
            // int rt=queries[t][2];
            // int ct=queries[t][3];    
            // for(int i=ro;i<=rt;i++)
            // {
            //     for(int j=co;j<=ct;j++)
            //     {
            //         ans[i][j]++;
            //     }
            // }
        int r1 = queries[t][0], c1 = queries[t][1], r2 = queries[t][2], c2 = queries[t][3];
        diff[r1][c1]++;
        if(r2+1 <n && c2+1 <n)    
          diff[r2 + 1][c2 + 1]++;
        if(c2+1 <n)    
           diff[r1][c2 + 1]--;
        if(r2+1<n)    
           diff[r2 + 1][c1]--;
       }

       for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
              int one =0;
              int two=0;
              int thr=0;
              if(i-1 >=0) 
                  one =diff[i - 1][j];
              if(j-1 >=0)
                  two=diff[i][j - 1];
              if(i-1>=0 && j-1>=0)
                  thr= diff[i - 1][j - 1];
            diff[i][j] += one + two - thr ;
            mat[i][j] += diff[i][j];
          }
        }
        return mat;
    }
};