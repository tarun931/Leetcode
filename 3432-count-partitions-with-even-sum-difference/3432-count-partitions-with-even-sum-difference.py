class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        sumi = sum(nums)
        if sumi%2 == 0:
            return len(nums)-1
        return 0  
        