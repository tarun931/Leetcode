class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
       long long max_sum = 0;
       long long min_sum=0; 
       long long sum = 0 ;
       for(int i=0;i<differences.size();i++)
       {
         sum += differences[i];
        if(sum<min_sum)
             min_sum = sum ;
        if(sum>max_sum)
             max_sum = sum ;           
       }
        long long t1 = lower - min_sum ;
        long long t2 = upper - max_sum ;
       long long min_start = max(1LL*lower,t1) ;
       long long max_start = min(1LL*upper,t2) ;
       return max(0LL, max_start-min_start+1);
    }
};