class Solution {
public:
    int helper(vector<int>& cost , int i)
    {
        if(i>=cost.size())
            return 0;
        return cost[i]+ min(helper(cost,i+1),helper(cost,i+2));    
    }
    int helper2(vector<int>& cost )
    {
      vector<int> dp(cost.size()+1,0);
      dp[0] = cost[0];
      dp[1] = cost[1];
      for(int i=2;i<cost.size();i++)
      {
         dp[i] = cost[i] + min(dp[i-1],dp[i-2]);
      }  
      return min(dp[cost.size()-1],dp[cost.size()-2]);
    }
    int helper3(vector<int>& cost )
    {
      int one  = cost[0];
      int two = cost[1];
      for(int i=2;i<cost.size();i++)
      {
        int three = 0;
         three = cost[i] + min(one,two);
         one = two ;
         two = three ;
      }  
      return min(one,two);
    }
    int minCostClimbingStairs(vector<int>& cost) {
        //return min(helper(cost , 0),helper(cost, 1));
        return helper3(cost);
    }
    //greedy will work here 
    // int minCostClimbingStairs(vector<int>& cost) {
    //      int n = cost.size();
        // for(int i = 2; i < n; i++){
        //     cost[i] +=  min(cost[i - 1], cost[i - 2]);
        // }

        // return min(cost[n - 1], cost[n - 2]);
    // }
};