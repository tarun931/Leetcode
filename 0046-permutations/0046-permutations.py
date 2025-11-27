from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # ans = []
        # def helper(start):
        #     if start>= n :
        #         ans.append(nums[:])
        #         return
        #     for i in range(start , len(nums)):
        #         nums[start], nums[i] = nums[i] , nums[start]
        #         helper(start+1)
        #         nums[start], nums[i] = nums[i] , nums[start]
            
        # helper(0)       
        # return ans
        all_perms = sorted(set(permutations(nums)))
        return all_perms    



        