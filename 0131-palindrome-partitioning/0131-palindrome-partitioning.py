class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def helper(i, arr):
            if i==n:
                ans.append(arr[:])
                return
            for j in range(i,n):
                sub = s[i:j+1]
                if sub == sub[::-1] :
                    arr.append(sub)
                    helper(j+1,arr)
                    arr.pop()
        helper(0,[])
        return ans                 
        