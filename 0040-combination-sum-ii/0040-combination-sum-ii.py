class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # ans = set().  # to use set , and tuple combo , its very expensive
        ans = []
        n = len(candidates)
        candidates.sort()
        def helper( i ,arr , cur):
            if cur == target :
                ans.append(arr[:])
                return
            if i>= n or cur>target :
                return 
            arr.append(candidates[i])
            helper(i+1, arr,cur+candidates[i])
            arr.pop()
            j = i + 1
            while j < n and candidates[j] == candidates[i]:   # skip duplicates
                j += 1
            helper(j , arr,cur)

        helper(0,[],0)
        return ans                



        