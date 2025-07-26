class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # ans , i = 0 , 0
        # while i <len(nums):
        #     if not nums[i]==0:
        #         i+=1
        #         continue
        #     res=1
        #     leng =1
        #     i+=1
        #     while i < len(nums) and nums[i]==0:
        #         leng +=1
        #         res+= leng
        #         i += 1
        #     ans += res    
        #     i+=1

        #simpler code
        ans,leng  = 0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                leng+=1
            else:
                leng = 0
            ans+=leng         
        return ans