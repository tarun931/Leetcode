class Solution:
    def maxProduct(self, n: int) -> int:
        li =  []
        num = n 
        while(num>0):
            li.append(int(num%10))
            num = num/10    
        li.sort()
        return li[-1]*li[-2]    
        