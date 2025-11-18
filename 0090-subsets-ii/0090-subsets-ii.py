class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        arr = []
        def helper(i , arr):
            if(i>=n):
                arr.sort()
                ans.add(tuple(arr))
                return
            #take
            arr.append(nums[i])
            helper(i+1,arr)
            arr.pop()
            helper(i+1,arr)
        
        helper(0,arr)
        return list([list(t) for t in ans])
        