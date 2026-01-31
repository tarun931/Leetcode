class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for i in range(0,len(letters)):
        #     if letters[i]> target:
        #         return letters[i]    

        # return letters[0]
        i  , j = 0 , len(letters)-1
        ans = -1
        while(i<=j):
            mid = (i+j+1)//2 
            if letters[mid] <= target:
                i = mid+1
            else:
                ans = mid
                j = mid-1       

        if ans == -1 :
            return letters[0]
        return letters[ans]              




        