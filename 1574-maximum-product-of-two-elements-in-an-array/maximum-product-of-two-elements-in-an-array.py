class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = max(nums[0], nums[1])
        ans = (nums[0]-1)* (nums[1]-1)
        for i in range(2 , len(nums)):
            if ans < (maxi-1)* (nums[i]-1):
                ans =  (maxi-1)* (nums[i]-1)
                maxi = max(maxi , nums[i])
        return ans        

        