class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for item in spells:
            low , hi = 0 , len(potions)-1
            m = -1
            while low<=hi:
                mid = (low+hi+1)//2
                
                if potions[mid]*item >= success:
                    m = mid
                    hi = mid-1
                else:
                    low = mid+1
            if m != -1:
                ans.append(len(potions)-m) 
            else:
                ans.append(0)                 
        return ans
        