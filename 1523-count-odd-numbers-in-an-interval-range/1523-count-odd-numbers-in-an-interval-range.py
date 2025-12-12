class Solution:
    def countOdds(self, low: int, high: int) -> int:
       return (high+(high&1)- low+(low&1))>>1
    # def countOdds(self, low: int, high: int) -> int:
    #    evenH , evenL = False ,False
    #    if high%2==0:
    #     evenH=True
    #    if low%2 == 0:
    #     evenL = True
    #    if evenH and evenL :
    #     return (high-low)//2
    #    return ((high-low)//2)+1 



