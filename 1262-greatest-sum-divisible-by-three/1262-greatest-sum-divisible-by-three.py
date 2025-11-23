class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a ,b , c = [],[],[]
        for ele in nums :
            if ele% 3 == 0:
                a.append(ele)
            elif ele%3 == 1:
                b.append(ele)
            else :
                c.append(ele)
        b.sort(reverse=True) 
        c.sort(reverse=True)
        ans = 0
        lb , lc = len(b) , len(c)
        for ele in [lb-1 , lb-2 , lb]:
            if ele >=0 :
                for ele2 in [lc-1 , lc-2 , lc]:
                    if ele2 >= 0 and (ele - ele2)% 3 == 0 :
                        ans = max(ans,sum(b[:ele])+ sum(c[:ele2]) )
        return ans + sum(a)                 

        
'''
in this question, out approach is :
make 3 arrays : a, b ,c made up of ele which give remainders 0,1,2 when divided by 3.
we can use all ele in a , since all the remainder will always. be 0
we can use a combo of elements in b and c  (1*cntb + 2*cntc)mod 3 , (one ele from b will give 1 remainder. ,lets say we choose cntb ele from b that means they will contri cntb*1 in remainder , and 2 elements(cntc=2) from c will give 2 remainders each ) .  We need to find a combo such that (1*cntb + 2*cntc) mod 3 == 0 . and also the largest sum. 
Now in b. ,there are only 3 remainders possible : sum(b) , sum(b-1) and sum(b-2) .  because , if we do sum(b-3)mod 3 == sum(b)mod 3 only , so to maximize sum ,only sum(b) , sum(b-1) and sum(b-2) will be considered .  Similarly in c , only sum(c) , sum(c-1) and sum(c-2)  are considered , because , only these 3 types of remainders are possible , either  0 ,2 , 4  , in case of sum(c-3)%3 will be same as sum(c)%3 only ,becuase (2 +2+2 )% 3 == 0 only. 
So in total we will try these 9 combo and get the best sum possible and add to sum(a). 
and that will be our final answer.  


'''
