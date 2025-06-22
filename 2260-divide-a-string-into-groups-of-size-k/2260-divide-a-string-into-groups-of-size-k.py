class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        size = len(s)
        ind = 0
        while ind < size:
            ans.append(s[ind:ind+k])
            ind += k
        n = len(ans)
        ans[-1] += fill *( k-len(ans[-1]))
        return ans               
