class Solution(object):
    def countNegatives(self, grid):
        negativecount=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]<0):
                    negativecount=negativecount+1
        return negativecount
        
