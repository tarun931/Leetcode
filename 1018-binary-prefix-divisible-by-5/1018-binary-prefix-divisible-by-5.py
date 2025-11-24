class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr = []
        num = 0 
        for i in range(len(nums)) :
            arr.append(num*2+nums[i])
            num  = num*2+nums[i]
        ans = []
        for ele in arr:
            if ele%5 ==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans                 


            

        