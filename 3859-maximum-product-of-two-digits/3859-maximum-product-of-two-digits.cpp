class Solution {
public:
     void maxi(int n , vector<int>& dig)
     {
        while(n>0)
        { 
            cout<<n%10 << " ";
            dig.push_back(n%10);
            n /= 10;
        }
        
     }
    int maxProduct(int n) {
       vector<int> dig;
       if(dig.size()==1)
          return dig[0];
       maxi( n ,dig);
       sort(dig.begin(),dig.end(),greater<int>());
       return dig[0]*dig[1]; 
    }
};