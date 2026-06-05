class Solution(object):
    def setZeroes(self, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col]==0):
                    
                    for cc in range(len(matrix[0])):
                        if(matrix[row][cc]!=0):
                            matrix[row][cc]=-99999
                    
                    for rc in range(len(matrix)):
                        if matrix[rc][col]!=0:
                            matrix[rc][col]=-99999
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j]==-99999:
                    matrix[i][j]=0



        
