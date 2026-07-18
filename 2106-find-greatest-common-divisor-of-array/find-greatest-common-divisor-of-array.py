class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi , mini = max(nums) , min(nums)
        return math.gcd(maxi, mini)

        