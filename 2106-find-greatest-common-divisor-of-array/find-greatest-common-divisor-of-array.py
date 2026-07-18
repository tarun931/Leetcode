class Solution:
    def gcd(self, a , b):
        while b:
            a,b = b , a%b
        return a    

    def findGCD(self, nums: List[int]) -> int:
        maxi , mini = max(nums) , min(nums)
        return gcd(mini , maxi)

        