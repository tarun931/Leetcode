class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = matrix[0][0]

        for j in range(0,len(matrix[0])):
            if matrix[0][j] == 0:
                col0 = 0
                break

        for i in range(0,len(matrix)):
            if matrix[i][0] == 0:
                matrix[0][0] = 0
                break 

        for j in range(1,len(matrix[0])):
                for i in range(1,len(matrix)):
                    if matrix[i][j] == 0:
                        # matrix[i][j] = 0
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for j in range(1,len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1,len(matrix)):
                    matrix[i][j] = 0

        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                for j in range(0,len(matrix[0])):
                    matrix[i][j]=0

        if col0 == 0:
            for j in range(1,len(matrix[0])):
                matrix[0][j]=0


        if matrix[0][0] == 0:
            for i in range(0,len(matrix)):
                matrix[i][0] = 0

        if col0 == 0: 
            matrix[0][0] = 0      

 


        # col = 1
        # for j in range(1,len(matrix[0])):
        #     if matrix[0][j] == 0:
        #         col0  = 0
        #         break

        # if col0 ==0 :
        #     for j in range(1,len(matrix[0])):
        #         matrix[0][j] = 0    


        # row = 1
        # for i in range(0,len(matrix)):
        #     if matrix[i][0] ==0:
        #         row = 0
        #         break 

        # if row == 0 :
        #     for i in range(0,len(matrix)):
        #         matrix[i][0] = 0    
        


            




        