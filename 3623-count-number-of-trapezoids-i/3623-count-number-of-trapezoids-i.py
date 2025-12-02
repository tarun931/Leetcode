class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        pt_ht = defaultdict(int)
        mod  = 10**9+7
        ans, total_sum = 0 , 0
        for point in points:
            pt_ht[point[1]] += 1

        for nums in pt_ht.values():
            edge = (nums * (nums-1))//2
            ans  = (ans + edge*total_sum)% mod  
            total_sum = (total_sum+edge)% mod
        return ans      


        