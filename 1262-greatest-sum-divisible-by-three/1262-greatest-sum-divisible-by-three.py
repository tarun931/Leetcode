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

        




                        
        