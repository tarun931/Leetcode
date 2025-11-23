# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         a ,b , c = [],[],[]
#         for ele in nums :
#             if ele% 3 == 0:
#                 a.append(ele)
#             elif ele%3 == 1:
#                 b.append(ele)
#             else :
#                 c.append(ele)
#         b.sort(reverse=True) 
#         c.sort(reverse=True)
#         ans = 0
#         lb , lc = len(b) , len(c)
#         for ele in [lb-1 , lb-2 , lb]:
#             if ele >=0 :
#                 for ele2 in [lc-1 , lc-2 , lc]:
#                     if ele2 >= 0 and (ele - ele2)% 3 == 0 :
#                         ans = max(ans,sum(b[:ele])+ sum(c[:ele2]) )
#         return ans + sum(a)                 

        
'''
in this question, out approach is :
make 3 arrays : a, b ,c made up of ele which give remainders 0,1,2 when divided by 3.
we can use all ele in a , since all the remainder will always. be 0
we can use a combo of elements in b and c  (1*cntb + 2*cntc)mod 3 , (one ele from b will give 1 remainder. ,lets say we choose cntb ele from b that means they will contri cntb*1 in remainder , and 2 elements(cntc=2) from c will give 2 remainders each ) .  We need to find a combo such that (1*cntb + 2*cntc) mod 3 == 0 . and also the largest sum. 
Now in b. ,there are only 3 remainders possible : sum(b) , sum(b-1) and sum(b-2) .  because , if we do sum(b-3)mod 3 == sum(b)mod 3 only , so to maximize sum ,only sum(b) , sum(b-1) and sum(b-2) will be considered .  Similarly in c , only sum(c) , sum(c-1) and sum(c-2)  are considered , because , only these 3 types of remainders are possible , either  0 ,2 , 4  , in case of sum(c-3)%3 will be same as sum(c)%3 only ,becuase (2 +2+2 )% 3 == 0 only. 
So in total we will try these 9 combo and get the best sum possible and add to sum(a). 
and that will be our final answer.  


'''

## DP

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0 , -float("inf") , -float("inf")]   # when we dont select anything , only acceptable solution is remainder=0(index=0) and sum= 0 (value at that index).Here indexes represents remainders , and value at that index represents the max sum we got for that remainder 
        for num in nums: # going through nums array(list)
            g  = f[:] # copy paste f in g , because we still require f .  for each num , we will make a new g and update f later 
            for i in range(3):
                g[(i+num%3)%3] = max(g[(i+num%3)%3],f[i]+num) # (i+num%3)%3 =  new remainder , suppose current i(rem)=1 , if we add 4%3 =1 , it becomes (1+1)%3 = 2 . so 2 is the remainder .
            f = g 
        return f[0]        


'''
g[(i+num%3)%3] = max(g[(i+num%3)%3],f[i]+num) , this means , we want to check , whether value of
g[new_remainder] is was more in f[new_remainder] or is it more when we add num to the f[i]

OR

f[i] + num = sum if we add this number to an old sum with remainder i
g[new_remainder] = best sum we have so far for this new remainder
Take the max → we always keep the largest possible sum for that remainder

In my language ;
[6 ,4 , 8 ]  : f  => remainder 0 , 1 , 2
g = f[:] = [6,4,8]
lets say num = 5 , rem =2 
suppose I add num to each of the numbers in f , we get. 
for num with rem =0  : , if we add 5 , new_rem = (0+2)% 3 = 2 
for num with rem =1 : , if we add 5 , new_rem = (1+2)% 3 = 0 
for num with rem =2 : if we add 5 , new_rem = (2+2)% 3 = 1 

so , now we will make a decision :
for g[0] , we had , sum = 6 , g[1] = 4 , g[2] = 8 , now we got , at g[0]  , new_sum = sum at rem = 1 previously in this case . "for num with rem =1 : , if we add 5 , new_rem = (1+2)% 3 = 0" , beaucse when I added 5 to this , then only we got new_rem = 0 , now we need to check , whether previous sum at remainder =1(previously) + 5 , = 4+5 = 9. 
hence 9> 6 , so we update g[0] = 9 > 6(previously).
similarly for g[1] = 8 + 5 = 13>4(previously) , and g[2] = 6+5 =11 > 8 (previously)
so now f = g
f = [9,13,8] , we have greatest sum with rem =0. => 9 , greatest sum with rem =1 =>13. , and rem =2 => sum = 8.

finally we will return greatest sum with rem=0
'''
