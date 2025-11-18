class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 0  ,   10
        # 1 1 , 0
        # if len(bits)==1:
        #     return True
        # elif (bits[0]==0):
        #     if bits[-2]!=1:
        #         return True
        #     return False
        # elif (bits[0]==1):
        #     if(len(bits)==2):   #
        #         return False
        #     elif((len(bits)-2)%2 != 0):
        #         return True 
        #     return False
        # return False  
        if len(bits)==1:
            return True
        if len(bits) ==2:
            if(bits[0]==0) :
                return True
            return False        
        if bits[-2] == 1:
            # if bits[-3] == 1:
            #     if len(bits)>=4:
            #         if bits[-4]==1:
            #             return False
            #         return True    
            #     else:
            #         return True
            # return False  
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


        