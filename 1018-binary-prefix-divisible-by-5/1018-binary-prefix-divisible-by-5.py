# class Solution:
#     def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
#         num = 0 
#         ans = []
#         for i in range(len(nums)) :
#             num  = num*2+nums[i]
#             if num%5 ==0:
#                 ans.append(True)
#             else:
#                 ans.append(False)
#         return ans  
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0 
        ans = []
        for ele in nums :
            num  = ((num<<1)+ele)%5
            ans.append(num==0)
        return ans                 


            

        