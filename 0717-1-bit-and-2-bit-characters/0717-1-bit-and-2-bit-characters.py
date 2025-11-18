class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1:
            return True
        if len(bits) ==2:
            if(bits[0]==0) :
                return True
            return False        
        if bits[-2] == 1:  
            count =0 
            i = -2
            while(len(bits) >= i*-1 and bits[i]== 1):
                count+=1
                i = i-1
            if count%2 == 0:
                return True
            return False        
        else:
            return True                    


        