class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        size = len(s)
        ind = 0
        # sol = ""
        # for i in s:
        #     if len(sol)==k:
        #         ans.append(sol)
        #         sol = ""
        #     sol += i 
        while ind < size:
            ans.append(s[ind:ind+k])
            ind += k
        # ans.append(sol)
        n = len(ans)
        # m = len(ans[-1])
        ans[-1] += fill *( k-len(ans[-1]))
        return ans               
