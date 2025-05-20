class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& q) {
        vector<int> sol(nums.size()+1,0);
        for(int i=0;i<q.size();i++)
        {
            int l = q[i][0];
            int r = q[i][1];
            sol[l] -= 1;
            sol[r+1] += 1;   //handle last ele 
        }
        int acc = 0;
        for(int i=0;i<=nums.size();i++)
        {
           sol[i] = acc + sol[i];
           acc = sol[i];
        }
        for(int i=0;i<nums.size();i++)
        {
            nums[i] = nums[i] + sol[i];
            if(nums[i]>0)
               return false;
        }
        return true;
    }
};