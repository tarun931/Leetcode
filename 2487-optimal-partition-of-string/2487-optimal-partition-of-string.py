class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        ans = 1
        for item in s:
            if item in cur:
                ans += 1
                cur = set()
            cur.add(item)
        return ans    
                    

        