class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return -1  
        one = nums[0]
        two , three = float('inf'), float('inf')
        ind = -1
        for i in range(1, n):
            if nums[i] < two:
                two = nums[i]
                ind = i

        for i in range(1, n):
            if nums[i]<three and i != ind:
                three = nums[i]

        return one + two + three               
        