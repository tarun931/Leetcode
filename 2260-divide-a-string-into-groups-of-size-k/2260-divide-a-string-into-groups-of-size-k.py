class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        sol = ""
        for i in s:
            if len(sol)==k:
                ans.append(sol)
                sol = ""
            sol += i    
        ans.append(sol)
        n = len(ans)
        m = len(ans[-1])
        ans[-1] += fill *( k-len(ans[-1]))
        return ans               
