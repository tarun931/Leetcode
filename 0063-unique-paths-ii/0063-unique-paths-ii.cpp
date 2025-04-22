class Solution {
public:
    int helper(vector<vector<int>>& oG)
    {
        int n = oG.size();
        int m = oG[0].size();
        oG[0][0]= 1;
        for(int i=1;i<oG[0].size();i++)
        {
            if(oG[0][i]==1)
                oG[0][i] = 0;
            else
                oG[0][i] = oG[0][i-1];    
        }
        for(int i=1;i<oG[0].size();i++)
        {
            cout<<oG[0][i]<<endl;    
        }
        for(int i=1;i<oG.size();i++)
        {
            if(oG[i][0]==1)
                oG[i][0] = 0;
            else
                oG[i][0] = oG[i-1][0] ;    
        }
        for(int i=1;i<oG.size();i++)
        {
            for(int j =1;j<oG[0].size();j++)
            {
               if(oG[i][j]==1)
                  oG[i][j] = 0 ;
               else 
                  oG[i][j] = oG[i-1][j]+ oG[i][j-1] ;
            }
        }
        return oG[n-1][m-1] ;
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if(obstacleGrid[0][0] == 1)
               return 0;
        return helper(obstacleGrid);
    }
};