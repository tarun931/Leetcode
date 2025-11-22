class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0 
        ans = 0
        for ele in nums:
            if ele%3 == 0:
                ans = ans 
            else:
                ans += 1
        return ans    
        