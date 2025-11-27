class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = 0
        maxi  = -sys.maxsize
        MinPreSum_rem = [sys.maxsize//2]*k
        MinPreSum_rem[k-1] = 0
        for i in range(n):
            prefixSum += nums[i]
            maxi = max(maxi , prefixSum-MinPreSum_rem[i%k])
            MinPreSum_rem[i%k] = min(MinPreSum_rem[i%k],prefixSum)
        return maxi    
             
        