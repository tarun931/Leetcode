class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem = 0
        for l in range(1,k+1): # if I am divinding a number by 3 , only possible remainders should be 0,1,2,. If we get 0 , we get our answer , but if we get 1,2 and then again if we get 1 or 2 , that means , we will never get 0 as the rem , it will forever stay in 1 and 2 . 
            rem = (rem*10+1)%k
            if rem==0:
                return l

        return -1        







        