class Solution:
    def numSub(self, s: str) -> int:
        ones =0 
        i =0
        ans = 0
        MOD = 10**9 + 7
        while(i< len(s)) :
           if (s[i] == '0' and ones=='0'):
            continue
           elif s[i]=='1':
            ones+=1 
           else:
            ans = (ans + (ones*(ones+1))//2 ) % MOD
            ones=0
           i+=1
        ans +=  ((ones*(ones+1))//2   ) % MOD
        return ans

        