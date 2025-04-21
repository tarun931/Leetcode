class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
       long long max_sum = INT_MIN;   //its better to use 0 
       long long min_sum=INT_MAX;     // its better to use 0
       long long sum = 0 ;
       for(int i=0;i<differences.size();i++)
       {
         sum += differences[i];
        if(sum<min_sum)
             min_sum = sum ;
        if(sum>max_sum)
             max_sum = sum ;           
       }
       long long min_start = max(1LL*lower,lower - min_sum) ;    //had i used max_suma nd min_sum =0 then it would be easier // check the code below 
       long long max_start = min(1LL*upper,upper - max_sum) ;
       return max(0LL, max_start-min_start+1);
    }
};

/*
int numberOfArrays(vector<int>& differences, int lower, int upper) 
    {
        long long minSum = 0, maxSum = 0, current = 0;

        for (int diff : differences) {
            current += diff;
            minSum = min(minSum, current);
            maxSum = max(maxSum, current);
        }

        long long minStart = lower - minSum;
        long long maxStart = upper - maxSum;

        return max(0LL, maxStart - minStart + 1);
        
    }
*/