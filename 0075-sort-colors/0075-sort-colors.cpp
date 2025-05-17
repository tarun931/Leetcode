class Solution {
public:
    void sortColors(vector<int>& nums) {
        int r=0;
        int b = 0;
        int w = 0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==0) r++;
            if(nums[i]==1) w++;
            if(nums[i]==2) b++;
        }
        int st= 0;
        while((r>0 || b>0 || w>0)&& st<nums.size())
        {
            if(r>0)
            {
                nums[st] = 0;
                st++;
                r--;
                continue;
            }
            else if(w>0)
            {
                nums[st] = 1;
                st++;
                w--;
                continue;
            }
            else if(b>0)
            {
                nums[st] = 2;
                st++;
                b--;
                continue;
            }
        }
    }
};