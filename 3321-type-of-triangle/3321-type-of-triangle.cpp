class Solution {
public:
    string triangleType(vector<int>& nums) {
       unordered_map<int,int> mp;
       int maxi=0;
    //    int maxi1 = 0;
    //    int maxi2= 0;
    //    int maxi3=INT_MAX;
       sort(nums.begin(),nums.end());
       for(auto x : nums)
       {
        mp[x]++;
        if(mp[x]>maxi)
            maxi= mp[x];
        // maxi1 = max(maxi1,x);
        // maxi3 = min(maxi1,x);    
       } 
       if(nums[0]+nums[1]<=nums[2])
            return "none";
       if(maxi==3)
           return "equilateral";
       else if(maxi==2)
           return "isosceles";    
       return "scalene"     ;  
    }
};