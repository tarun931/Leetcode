class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long cnt1 = 0;
        long long cnt2 = 0;
        long long sum1 = 0;
        long long sum2 = 0;
        for(int i=0;i<nums1.size();i++)
        {
            if(nums1[i]==0){
                cnt1++;
                sum1++;
            }    
            sum1 += nums1[i];    
        }
        cout<<cnt1<<" "<<sum1<<endl;
        for(int i=0;i<nums2.size();i++)
        {
            if(nums2[i]==0){
                cnt2++;
                sum2++;
            }    
            sum2 += nums2[i];
                
        }
        if(cnt1==0 && sum1<sum2 || cnt2==0 && sum2<sum1)
              return -1;

        return max(sum1,sum2);
    }
};