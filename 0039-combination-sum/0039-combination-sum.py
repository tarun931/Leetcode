class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        n = len(candidates)
        def helper(i, arr , target):
            if target == 0:
                # arr.sort()
                ans.add(tuple(arr)) #is we hadnt used set , then we could have used a list  , arr[:] , in this way 
                return 
            elif target <0 :
                return  
            if i<n:      
                arr.append(candidates[i])
                helper(i,arr , target-candidates[i])
                arr.pop()
                helper(i+1 , arr , target)
        helper(0,[],target)    
        return list(list(t) for t in ans)        
        