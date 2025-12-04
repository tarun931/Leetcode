class Solution:
    def countCollisions(self, directions: str) -> int:
        n= len(directions)
        i = 0
        leadingLs = 0
        while i < n and directions[i]=='L':
            i+=1
        leading_L = i
        leading_R =0
        i= n-1
        while i > -1 and directions[i] =='R':
            i = i-1
        leading_R  = n-1- i

        tot = sum(1 for c in directions if c!='S')
        return tot - leading_L-leading_R   

    
     
         



