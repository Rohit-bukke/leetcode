class Solution(object):
    def removeDuplicates(self, arr):
        i=0
        n=len(arr)
        for j in range(1,n):
            if (arr[j]!=arr[i]):
                i=i+1
                arr[i]= arr[j]

        return i+1
        
