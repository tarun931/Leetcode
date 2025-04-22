class Solution {
public:
    // int helper(vector<int>& cost , int i)
    // {
    //     if(i>=cost.size())
    //         return 0;
    //     return cost[i]+ min(helper(cost,i+1),helper(cost,i+2));    
    // }
    int minCostClimbingStairs(vector<int>& cost) {
        //return min(helper(cost , 0),helper(cost, 1));
        int n = cost.size();

        for(int i = 2; i < n; i++){
            cost[i] +=  min(cost[i - 1], cost[i - 2]);
        }

        return min(cost[n - 1], cost[n - 2]);
    }
};