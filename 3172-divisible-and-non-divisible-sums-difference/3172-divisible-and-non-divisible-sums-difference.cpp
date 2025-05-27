class Solution {
public:
    int differenceOfSums(int n, int m) {
        float t= (float)n*(((float)n+1.0)/2.0);
        int sum = int(t); 
        cout<<sum<<" ";
        if(m==1)
           return -sum;
        int i = m ;
        int s = 0;
        while(i<=n)
        {
          s += i ;
          i+=m;
        }
        int nd = sum-s;
        cout<<nd<<" "<<s;
        return nd-s;
    }
};