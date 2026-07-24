class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = max(nums)
        u = 1
        while u <= m:
            u <<= 1
        one = [False] * u
        two = [False] * u
        three = [False] * u
        for v in nums:
            one[v] = True
            for x in range(u):
                if one[x]:
                    two[x ^ v] = True
        for v in nums:
            for x in range(u):
                if two[x]:
                    three[x ^ v] = True
        return sum(1 for b in three if b)