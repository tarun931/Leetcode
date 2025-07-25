class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxi = nums[0]
        sumi = maxi
        for i in range(1,len(nums)):
            # if nums[i]<= maxi:
            #     continue
            sumi += nums[i]
            avg = (sumi)/(i+1)
            maxi = max(math.ceil(avg),maxi)

        return maxi      

            


            

        