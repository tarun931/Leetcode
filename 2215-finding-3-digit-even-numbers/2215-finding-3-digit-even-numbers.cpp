class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> ans;
        unordered_map<int,int>mp;
        for(int i=0;i<digits.size();i++)
        {
            int one = digits[i];
            //cout<<one<<" ";
            if(one==0)
                continue;
            int two = -1;
            int three = -1;
            for(int j=0;j<digits.size();j++)
            {
               if(j==i)
                  continue;
                  
               two = digits[j];
               //cout<<two<<" ";
               for(int k = 0;k<digits.size();k++)
               {
                if(k==i || k==j || (digits[k]%2!=0))
                   continue;
                three = digits[k];
                //cout<<three<<" "<<k<<endl;
                if(two == -1 || three == -1)
                     continue;
                  int n = one*100 + two*10 + three;
                 if(n>=100 && n%2==0 && mp.find(n)==mp.end()){
                      ans.push_back(n);
                      //cout<<n<<endl;
                      mp[n]++;
                 }    
               }
            }
                   
        }
        sort(ans.begin(),ans.end());
        return ans;
    }
};