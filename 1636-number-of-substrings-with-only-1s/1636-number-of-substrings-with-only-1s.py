class Solution:
    def numSub(self, s: str) -> int:
        ones , i ,ans,  MOD =0 , 0 ,0 , 10**9+7 
        while(i< len(s)) :
           if (s[i] == '0'):
            ans = (ans + (ones*(ones+1))//2 ) % MOD
            ones=0
           else :
            ones+=1 
           i+=1
        ans =  (ans+((ones*(ones+1))//2 )) % MOD
        return ans

        