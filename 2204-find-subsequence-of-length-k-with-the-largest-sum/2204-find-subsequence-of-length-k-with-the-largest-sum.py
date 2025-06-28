class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i,nums[i]] for i in range(0,n)]
        vals.sort(key = lambda x:-x[1])
        vals = sorted(vals[: k])
        vals = [ val for i,val in vals ]
        return vals
        